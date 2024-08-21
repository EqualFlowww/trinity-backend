# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from fastapi import WebSocketDisconnect

from common import MeshControl, AsyncRest

from schema.demo.device import Cart
from schema.demo.operation import Round
from schema.demo.chat import Message


#===============================================================================
# Implement
#===============================================================================
class Control(MeshControl):

    def __init__(self, modPath):
        MeshControl.__init__(self, modPath=modPath)

        kcHostname = self.config['keycloak']['hostname']
        kcHostport = self.config['keycloak']['port']
        self._kcBaseUrl = f'http://{kcHostname}:{kcHostport}'
        self._sockets = {}
        self._admins = []

    async def startup(self):
        await self.registerModel(Cart, 'uerp')
        await self.registerModel(Round, 'uerp')

    async def shutdown(self): pass

    async def sendDataToUsername(self, username, key, value):
        if username not in self._sockets: return None
        payload = {'k': key, 'v': value}
        if username in self._sockets:
            for socket in self._sockets[username]:
                try: await socket.send_json(payload)
                except Exception as e: LOG.ERROR(e)
        return payload

    async def sendDataToAdmin(self, key, value):
        payload = {'k': key, 'v': value}
        for socket in self._admins:
            try: await socket.send_json(payload)
            except Exception as e: LOG.ERROR(e)
        return payload

    async def registerAdminConnection(self, socket, token, org):
        async with AsyncRest(self._kcBaseUrl) as rest:
            userinfo = await rest.get(f'/realms/{org}/protocol/openid-connect/userinfo', headers={'Authorization': f'Bearer {token}'})
        username = userinfo['preferred_username']
        await socket.accept()
        if username not in self._sockets: self._sockets[username] = []
        if socket not in self._sockets[username]: self._sockets[username].append(socket)
        if socket not in self._admins: self._admins.append(socket)
        while True:
            try: await self.parseAdminData(token, org, await socket.receive_json())
            except WebSocketDisconnect:
                self._sockets[username].remove(socket)
                self._admins.remove(socket)
                break
            except Exception as e:
                LOG.ERROR(e)
                self._sockets[username].remove(socket)
                self._admins.remove(socket)
                await socket.close()
                break

    async def parseAdminData(self, token, org, data):
        LOG.DEBUG(1)

        key = data['k']
        val = data['v']

        LOG.DEBUG(2)

        if key == 'msg':

            LOG.DEBUG(3)

            roomId = val['roomId']

            LOG.DEBUG(4)

            unreadUsernames = val['unreadUsernames']

            LOG.DEBUG(5)

            message = Message(
                content=val['content'],
                username=val['username'],
                roomId=roomId,
                unreadUsernames=unreadUsernames
            )

            LOG.DEBUG(message)

            message = await message.createModel(token, org)

            LOG.DEBUG(7)

            message = message.model_dump()

            LOG.DEBUG(8)

            for username in unreadUsernames:
                await self.sendDataToUsername(username, 'md', message)

    async def registerCartConnection(self, socket, token, org, cartId):
        async with AsyncRest(self._kcBaseUrl) as rest:
            userinfo = await rest.get(f'/realms/{org}/protocol/openid-connect/userinfo', headers={'Authorization': f'Bearer {token}'})
        username = userinfo['preferred_username']
        await socket.accept()
        if username not in self._sockets: self._sockets[username] = []
        if socket not in self._sockets[username]: self._sockets[username].append(socket)
        cart = await Cart.readModelByID(cartId, token=token, org=org)
        await self.sendDataToUsername(username, 'md', cart.model_dump())
        while True:
            try: await self.parseCartData(token, org, cartId, await socket.receive_json())
            except WebSocketDisconnect:
                self._sockets[username].remove(socket)
                break
            except Exception as e:
                LOG.ERROR(e)
                self._sockets[username].remove(socket)
                await socket.close()
                break

    async def parseCartData(self, token, org, cartId, data):
        if data['k'] == 'gps':
            cart = await Cart.readModelByID(cartId, token=token, org=org)
            lat, lon = data['v']
            cart.location.x = lon
            cart.location.y = lat
            cart = (await cart.updateModel(token=token, org=org)).model_dump()
            await self.sendDataToAdmin('md', cart)

