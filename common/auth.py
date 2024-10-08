# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from pydantic import BaseModel

from .constants import SECONDS, AAA
from .models import Option, SchemaConfig, Key, EmptyReference, BaseSchema, ProfSchema, Reference


#===============================================================================
# Implement
#===============================================================================
class AuthInfo(BaseModel):

    org: str = ''
    username: str = ''
    admin: bool = False
    policy: list[str] = []
    aclRead: list[str] = []
    aclCreate: list[str] = []
    aclUpdate: list[str] = []
    aclDelete: list[str] = []

    def checkOrg(self, org): return True if self.org == org else False

    def checkUsername(self, username): return True if self.username == username else False

    def checkAccount(self, realm, username): return True if self.realm == realm and self.owner == username else False

    def checkAdmin(self): return self.admin

    def checkPolicy(self, policy): return True if policy in self.policy else False

    def checkReadACL(self, sref): return True if sref in self.aclRead else False

    def checkCreateACL(self, sref): return True if sref in self.aclCreate else False

    def checkUpdateACL(self, sref): return True if sref in self.aclUpdate else False

    def checkDeleteACL(self, sref): return True if sref in self.aclDelete else False


@SchemaConfig(
version=1,
aaa=AAA.AA,
cache=Option(expire=SECONDS.HOUR),
search=Option(expire=SECONDS.DAY))
class Org(BaseModel, BaseSchema):

    externalId: Key = ''
    name: Key = ''
    displayName: str = ''


@SchemaConfig(
version=1,
aaa=AAA.AA,
cache=Option(expire=SECONDS.HOUR),
search=Option(expire=SECONDS.DAY))
class Account(BaseModel, BaseSchema):

    externalId: Key = ''
    username: str = ''
    displayName: str = ''
    givenName: str = ''
    familyName: str = ''
    email: str = ''
    policy: list[str] = []
    detail: Reference = EmptyReference


@SchemaConfig(
version=1,
aaa=AAA.AA,
cache=Option(expire=SECONDS.HOUR),
search=Option(expire=SECONDS.DAY))
class Policy(BaseModel, ProfSchema, BaseSchema):

    externalId:Key = ''

    aclRead: list[str] = []
    aclCreate: list[str] = []
    aclUpdate: list[str] = []
    aclDelete: list[str] = []


@SchemaConfig(
version=1,
aaa=AAA.AA,
cache=Option(expire=SECONDS.HOUR),
search=Option(expire=SECONDS.DAY))
class Group(BaseModel, ProfSchema, BaseSchema):

    externalId: Key = ''
    parentId: Key = ''
