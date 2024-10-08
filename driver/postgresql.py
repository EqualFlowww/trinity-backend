# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
import json
import inspect
from uuid import UUID
from pydantic import BaseModel
from stringcase import snakecase
from psycopg import AsyncConnection
from luqum.tree import Item, Term, SearchField, Group, FieldGroup, Range, From, To, AndOperation, OrOperation, Not, UnknownOperation

from common import asleep, runBackground, EpException, BaseSchema, Search, ModelDriverBase


#===============================================================================
# Implement
#===============================================================================
class PostgreSql(ModelDriverBase):

    def __init__(self, config):
        ModelDriverBase.__init__(self, config)

        self._psqlUsername = config['default']['system_access_key']
        self._psqlPassword = config['default']['system_secret_key']

        self._psqlHostname = config['postgresql']['hostname']
        self._psqlHostport = int(config['postgresql']['port'])
        self._psqlDatabase = config['postgresql']['database']

        self._psql = None
        self._psqlConnMutex = False

    async def connect(self, *args, **kargs):
        if not self._psql:
            self._psql = await AsyncConnection.connect(
                host=self._psqlHostname,
                port=self._psqlHostport,
                dbname=self._psqlDatabase,
                user=self._psqlUsername,
                password=self._psqlPassword
            )
        return self

    async def disconnect(self):
        if self._psql:
            try: await self._psql.close()
            except: pass
            self._psql = None
        if self._psql:
            try: await self._psql.close()
            except: pass
            self._psql = None

    async def reconnect(self):
        if not self._psqlConnMutex:
            self._psqlConnMutex = True
            await runBackground(self.__restore_background__())

    async def __restore_background__(self):
        while True:
            await asleep(1)
            await self.disconnect()
            try: await self.connect()
            except: continue
            break
        self._psqlConnMutex = False

    def __parseLuceneToTsquery__(self, node:Item):
        nodeType = type(node)
        if isinstance(node, Term):
            terms = filter(None, str(node.value).strip('"').lower().split(' '))
            return f"{'|'.join(terms)}"
        elif nodeType == SearchField:
            if '.' in node.name: fieldName = snakecase(node.name.split('.')[0])
            else: fieldName = snakecase(node.name)
            exprType = type(node.expr)
            if exprType in [Range, From, To]:
                if exprType == Range: return f'{fieldName} >= {node.expr.low} AND {fieldName} <= {node.expr.high}'
                elif exprType == From: return f"{fieldName} >{'=' if node.expr.include else ''} {node.expr.a}"
                elif exprType == To: return f"{fieldName} <{'=' if node.expr.include else ''} {node.expr.a}"
            else:
                result = self.__parseLuceneToTsquery__(node.expr)
                if result: return f"{fieldName}@@to_tsquery('{result}')"
            return None
        elif nodeType == Group:
            result = self.__parseLuceneToTsquery__(node.expr)
            if result: return f'({result})'
            return None
        elif nodeType == FieldGroup:
            return self.__parseLuceneToTsquery__(node.expr)
        elif nodeType == AndOperation:
            operand1 = node.operands[0]
            operand2 = node.operands[1]
            result1 = self.__parseLuceneToTsquery__(operand1)
            result2 = self.__parseLuceneToTsquery__(operand2)
            if result1 and result2:
                if (isinstance(operand1, Term) or type(operand1) == Not) and (isinstance(operand2, Term) or type(operand2) == Not): return f'{result1}&{result2}'
                else: return f'{result1} AND {result2}'
            return None
        elif nodeType == OrOperation:
            operand1 = node.operands[0]
            operand2 = node.operands[1]
            result1 = self.__parseLuceneToTsquery__(operand1)
            result2 = self.__parseLuceneToTsquery__(operand2)
            if result1 and result2:
                if (isinstance(operand1, Term) or type(operand1) == Not) and (isinstance(operand2, Term) or type(operand2) == Not): return f'{result1}|{result2}'
                else: return f'{result1} OR {result2}'
            return None
        elif nodeType == Not:
            result = self.__parseLuceneToTsquery__(node.a)
            if result:
                if isinstance(node.a, Term): return f'!{result}'
                else: return f'NOT {result}'
            return None
        elif nodeType == UnknownOperation:
            if hasattr(node, 'operands'):
                operand = str(node.operands[1]).upper()
                if operand == 'AND': opermrk = '&'
                elif operand == 'OR': opermrk = '|'
                elif operand == '&':
                    opermrk = operand
                    operand = 'AND'
                elif operand == '|':
                    opermrk = operand
                    operand = 'OR'
                else: raise EpException(400, f'Could Not Parse Filter: {node} >> {nodeType}{node.__dict__}')
                operand1 = node.operands[0]
                operand2 = node.operands[2]
                if (isinstance(operand1, Term) or type(operand1) == Not) and (isinstance(operand2, Term) or type(operand2) == Not):
                    return f"{self.__parseLuceneToTsquery__(operand1)}{opermrk}{self.__parseLuceneToTsquery__(operand2)}"
                else:
                    return f"{self.__parseLuceneToTsquery__(operand1)} {operand} {self.__parseLuceneToTsquery__(operand2)}"
        raise EpException(400, f'Could Not Parse Filter: {node} >> {nodeType}{node.__dict__}')

    def __json_dumper__(self, d): return "'" + json.dumps(d, separators=(',', ':')).replace("'", "\'") + "'"

    def __text_dumper__(self, d): return f"'{str(d)}'"

    def __data_dumper__(self, d): return str(d)

    def __json_loader__(self, d): return json.loads(d)

    def __data_loader__(self, d): return d

    async def registerModel(self, schema:BaseSchema, *args, **kargs):
        info = schema.getSchemaInfo()
        fields = sorted(schema.model_fields.keys())
        snakes = [snakecase(field) for field in fields]

        index = 0
        columns = []
        dumpers = []
        loaders = []
        indices = {}
        for field in fields:
            fieldType = schema.model_fields[field].annotation
            if fieldType == str:
                columns.append(f'{snakes[index]} TEXT')
                dumpers.append(self.__text_dumper__)
                loaders.append(self.__data_loader__)
                indices[fields[index]] = index
            elif fieldType == int:
                columns.append(f'{snakes[index]} INTEGER')
                dumpers.append(self.__data_dumper__)
                loaders.append(self.__data_loader__)
                indices[fields[index]] = index
            elif fieldType == float:
                columns.append(f'{snakes[index]} DOUBLE PRECISION')
                dumpers.append(self.__data_dumper__)
                loaders.append(self.__data_loader__)
                indices[fields[index]] = index
            elif fieldType == bool:
                columns.append(f'{snakes[index]} BOOL')
                dumpers.append(self.__data_dumper__)
                loaders.append(self.__data_loader__)
                indices[fields[index]] = index
            elif fieldType == UUID:
                if field == 'id': columns.append(f'id TEXT PRIMARY KEY')
                else: columns.append(f'{snakes[index]} TEXT')
                dumpers.append(self.__text_dumper__)
                loaders.append(self.__data_loader__)
                indices[fields[index]] = index
            elif (inspect.isclass(fieldType) and issubclass(fieldType, BaseModel)):
                columns.append(f'{snakes[index]} TEXT')
                dumpers.append(self.__json_dumper__)
                loaders.append(self.__json_loader__)
                indices[fields[index]] = index
            elif fieldType in [list, dict]:
                columns.append(f'{snakes[index]} TEXT')
                dumpers.append(self.__json_dumper__)
                loaders.append(self.__json_loader__)
                indices[fields[index]] = index
            elif getattr(fieldType, '__origin__', None) in [list, dict]:
                columns.append(f'{snakes[index]} TEXT')
                dumpers.append(self.__json_dumper__)
                loaders.append(self.__json_loader__)
                indices[fields[index]] = index
            else: raise EpException(500, f'database.registerModel({schema}.{field}{fieldType}): could not parse schema')
            index += 1

        info.database['fields'] = fields
        info.database['snakes'] = snakes
        info.database['dumpers'] = dumpers
        info.database['loaders'] = loaders
        info.database['indices'] = indices

        try: await self.connect()
        except: exit(1)
        async with self._psql.cursor() as cursor:
            await cursor.execute(f"CREATE TABLE IF NOT EXISTS {info.dref} ({','.join(columns)});")
            await self._psql.commit()

    async def read(self, schema:BaseSchema, id:str):
        info = schema.getSchemaInfo()

        query = f"SELECT * FROM {info.dref} WHERE id='{id}' AND deleted=FALSE LIMIT 1;"
        cursor = self._psql.cursor()
        try:
            await cursor.execute(query)
            record = await cursor.fetchone()
        except Exception as e:
            await cursor.close()
            await self.reconnect()
            raise e
        await cursor.close()

        if record:
            fields = info.database['fields']
            loaders = info.database['loaders']
            index = 0
            model = {}
            for column in record:
                model[fields[index]] = loaders[index](column)
                index += 1
            return model
        return None

    async def search(self, schema:BaseSchema, search:Search):
        info = schema.getSchemaInfo()
        unique = False

        if search.fields:
            termFields = [field.split('.')[0] for field in search.fields]
            columns = ','.join([snakecase(field) for field in termFields])
        else: columns = '*'
        if search.filter:
            filter = self.__parseLuceneToTsquery__(search.filter)
            if filter: filter = [filter]
            else: filter = []
        else: filter = []
        condition = ' AND '.join(filter)
        if condition: condition = f' AND {condition}'
        if search.orderBy and search.order: condition = f'{condition} ORDER BY {snakecase(search.orderBy)} {search.order.upper()}'
        if search.size:
            if search.size == 1: unique = True
            condition = f'{condition} LIMIT {search.size}'
        if search.skip: condition = f'{condition} OFFSET {search.skip}'
        query = f'SELECT {columns} FROM {info.dref} WHERE deleted=FALSE{condition};'

        cursor = self._psql.cursor()
        try:
            await cursor.execute(query)
            if unique:
                records = await cursor.fetchone()
                if records: records = [records]
                else: records = []
            else: records = await cursor.fetchall()
        except Exception as e:
            await cursor.close()
            await self.reconnect()
            raise e
        await cursor.close()

        fields = info.database['fields']
        loaders = info.database['loaders']
        models = []
        if search.fields:
            indices = info.database['indices']
            for record in records:
                index = 0
                model = {}
                for column in record:
                    fieldIndex = indices[termFields[index]]
                    model[fields[fieldIndex]] = loaders[fieldIndex](column)
                    index += 1
                models.append(model)
        else:
            for record in records:
                index = 0
                model = {}
                for column in record:
                    model[fields[index]] = loaders[index](column)
                    index += 1
                models.append(model)
        return models

    async def count(self, schema:BaseSchema, search:Search):
        info = schema.getSchemaInfo()

        if search.filter:
            filter = self.__parseLuceneToTsquery__(search.filter)
            if filter: filter = [filter]
            else: filter = []
        else: filter = []
        condition = ' AND '.join(filter)
        if condition: condition = f' AND {condition}'
        query = f'SELECT COUNT(*) FROM {info.dref} WHERE deleted=FALSE{condition};'

        cursor = self._psql.cursor()
        try:
            await cursor.execute(query)
            count = await cursor.fetchone()
        except Exception as e:
            await cursor.close()
            await self.reconnect()
            raise e
        await cursor.close()
        return count[0]

    async def create(self, schema:BaseSchema, *models):
        if models:
            info = schema.getSchemaInfo()
            fields = info.database['fields']
            dumpers = info.database['dumpers']
            cursor = self._psql.cursor()
            try:
                for model in models:
                    index = 0
                    values = []
                    for field in fields:
                        values.append(dumpers[index](model[field]))
                        index += 1
                    query = f"INSERT INTO {info.dref} VALUES({','.join(values)});"
                    await cursor.execute(query)
                    await cursor.execute(f"SELECT COUNT(*) FROM {info.dref} WHERE id='{model['id']}';")
                results = [bool(result) for result in await cursor.fetchall()]
                await self._psql.commit()
            except Exception as e:
                await cursor.close()
                await self.reconnect()
                raise e
            await cursor.close()
            return results
        return []

    async def update(self, schema:BaseSchema, *models):
        if models:
            info = schema.getSchemaInfo()
            fields = info.database['fields']
            snakes = info.database['snakes']
            dumpers = info.database['dumpers']
            cursor = self._psql.cursor()
            try:
                for model in models:
                    id = model['id']
                    index = 0
                    values = []
                    for field in fields:
                        value = dumpers[index](model[field])
                        values.append(f'{snakes[index]}={value}')
                        index += 1
                    query = f"UPDATE {info.dref} SET {','.join(values)} WHERE id='{id}' AND deleted=FALSE;"
                    await cursor.execute(query)
                    await cursor.execute(f"SELECT COUNT(*) FROM {info.dref} WHERE id='{id}' AND deleted=FALSE;")
                results = [bool(result) for result in await cursor.fetchall()]
                await self._psql.commit()
            except Exception as e:
                await cursor.close()
                await self.reconnect()
                raise e
            await cursor.close()
            return results
        return []

    async def delete(self, schema:BaseSchema, id:str):
        info = schema.getSchemaInfo()
        query = f"DELETE FROM {info.dref} WHERE id='{id}';"
        cursor = self._psql.cursor()
        try:
            await cursor.execute(query)
            await cursor.execute(f"SELECT COUNT(*) FROM {info.dref} WHERE id='{id}';")
            result = [bool(not result[0]) for result in await cursor.fetchall()][0]
            await self._psql.commit()
        except Exception as e:
            await cursor.close()
            await self.reconnect()
            raise e
        await cursor.close()
        return result
