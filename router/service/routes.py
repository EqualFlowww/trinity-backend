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
    await ctrl.registerAdminConnection(socket, token, org)


@api.websocket(f'{ctrl.uri}/websocket/cart/{{cartId}}')
async def connect_cart_websocket(
    socket:WebSocket,
    cartId:UUID,
    token: str,
    org: str | None=None
):
    await ctrl.registerCartConnection(socket, token, org, str(cartId))
