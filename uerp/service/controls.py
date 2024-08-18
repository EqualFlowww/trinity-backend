# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from common import UerpControl

from driver.auth_kc_redis import AuthKeyCloakRedis
from driver.redis import RedisModel
from driver.elasticsearch import ElasticSearch
from driver.postgresql import PostgreSql

from schema.demo.device import Cart
from schema.demo.operation import Round


#===============================================================================
# Implement
#===============================================================================
class Control(UerpControl):

    def __init__(self, modPath):
        UerpControl.__init__(
            self,
            modPath=modPath,
            authDriver=AuthKeyCloakRedis,
            cacheDriver=RedisModel,
            searchDriver=ElasticSearch,
            databaseDriver=PostgreSql
        )

    async def startup(self):
        await self.registerModel(Cart)
        await self.registerModel(Round)

    async def shutdown(self): pass
