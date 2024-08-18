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
class CurrentHole(BaseModel):
    number:int = 0
    courseType:Key = ''
    startTime:str = ''
    elapsedTime:str = ''
    scheduledEndTime:str = ''


@SchemaConfig(
version=1,
aaa=AAA.A,
cache=Option(expire=SECONDS.HOUR),
search=Option(expire=SECONDS.DAY))
class Round(BaseModel, ProfSchema, BaseSchema):
    half:Key = ''
    roundOrder:Key = ''
    isVip:bool = False
    isNineHolePlus:bool = False
    currentHole:CurrentHole
    cartIdList:list[str] = []

