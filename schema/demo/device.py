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
class CartManager(BaseModel):
    name:Key = ''
    type:Key = ''


class GpsLocation(BaseModel):
    x:float = 0.0
    y:float = 0.0


@SchemaConfig(
version=1,
aaa=AAA.A,
cache=Option(expire=SECONDS.HOUR),
search=Option(expire=SECONDS.DAY))
class Cart(BaseModel, ProfSchema, BaseSchema):
    type:Key = ''
    manager:CartManager
    isWarning:bool = False
    isBatteryAlert:bool = False
    isPersonAlert:bool = False
    location:GpsLocation
    roundId:Key = ''

