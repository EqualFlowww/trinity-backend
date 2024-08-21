# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from pydantic import BaseModel
from common import SECONDS, AAA, SchemaConfig, Option, Key, BaseSchema, ProfSchema


#===============================================================================
# Implement
#===============================================================================
@SchemaConfig(
version=3,
aaa=AAA.A,
cache=Option(expire=SECONDS.HOUR),
search=Option(expire=SECONDS.DAY))
class Message(BaseModel, BaseSchema):
    content:str = ''
    username:Key = ''
    roomId:Key = ''
    unreadUsernames:list[str] = []


@SchemaConfig(
version=3,
aaa=AAA.A,
cache=Option(expire=SECONDS.HOUR),
search=Option(expire=SECONDS.DAY))
class Room(BaseModel, ProfSchema, BaseSchema):
    type:Key = ''
    participants:list[str] = []
