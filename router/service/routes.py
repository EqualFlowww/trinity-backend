# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
import os

from fastapi import WebSocket, WebSocketDisconnect
from uuid import UUID

from .controls import Control

from schema.demo.device import Cart

#===============================================================================
# SingleTone
#===============================================================================
ctrl = Control(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
api = ctrl.api


#===============================================================================
# API Interfaces
#===============================================================================
@api.websocket(f'{ctrl.uri}/websocket/admin')
async def connect_admin_websocket(
    socket:WebSocket,
    token: str,
    org: str | None=None
):
    await socket.accept()
    ctrl.adminSockets.append(socket)
    while True:
        try:
            await ctrl.parseAdminData(await socket.receive_json())
        except WebSocketDisconnect:
            ctrl.adminSockets.remove(socket)
            break


@api.websocket(f'{ctrl.uri}/websocket/cart/{{cartId}}')
async def connect_cart_websocket(
    socket:WebSocket,
    cartId:UUID,
    token: str,
    org: str | None=None
):
    cartId = str(cartId)
    LOG.DEBUG(org)
    LOG.DEBUG(token)
    LOG.DEBUG(cartId)
    cart = await Cart.readModelByID(cartId, token=token, org=org)
    LOG.DEBUG(cart)
    LOG.DEBUG('DONE')

    await socket.accept()
    if cartId not in ctrl.cartSockets: ctrl.cartSockets[cartId] = []
    ctrl.cartSockets[cartId].append(socket)
    while True:
        try:
            await socket.send_json(cart.model_dump())
            await ctrl.parseCartData(cartId, token, org, await socket.receive_json())
        except WebSocketDisconnect:
            ctrl.cartSockets[cartId].remove(socket)
            break
