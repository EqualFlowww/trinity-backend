# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from common import MeshControl

from schema.demo.device import Cart
from schema.demo.operation import Round


#===============================================================================
# Implement
#===============================================================================
class Control(MeshControl):

    def __init__(self, modPath):
        MeshControl.__init__(
            self,
            modPath=modPath
        )

        self.adminSockets = []
        self.cartSockets = {}

    async def startup(self):
        await self.registerModel(Cart, 'uerp')
        await self.registerModel(Round, 'uerp')

    async def shutdown(self): pass

    async def parseAdminData(self, data):
        pass

    async def parseCartData(self, cartId, token, org, data):
        cart = await Cart.readModelByID(cartId, token=token, org=org)
        if data['type'] == 'gps':
            x, y = data['body']
            cart.location.x = x
            cart.location.y = y
        cart = await cart.updateModel(token=token, org=org)
        for socket in self.adminSockets:
            await socket.send_json(cart.model_dump())
