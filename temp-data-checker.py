# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
import json
import requests

#===============================================================================
# Implement
#===============================================================================
baseUrl = 'https://trinity.eqpls.net'
token = 'eyJhbGciOiJIUzUxMiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJiMzUzNjMyNS1kYWFlLTRlNWQtYjZjNS1lMzJhMTMzM2IzZDEifQ.eyJleHAiOjE3MjQxNDg3NDQsImlhdCI6MTcyNDE0Njk0NCwianRpIjoiYWUyNzFkMzUtNTAyYS00YjVmLWI3ZTUtM2I4NDBhYTg0ZmVlIiwiaXNzIjoiaHR0cHM6Ly90cmluaXR5LmVxcGxzLm5ldC9hdXRoL3JlYWxtcy90cmluaXR5IiwiYXVkIjoiaHR0cHM6Ly90cmluaXR5LmVxcGxzLm5ldC9hdXRoL3JlYWxtcy90cmluaXR5Iiwic3ViIjoiYWVlNzE3NDQtNjlmZS00NTIwLTk4MTAtYjU1M2MzZDBjMjVhIiwidHlwIjoiUmVmcmVzaCIsImF6cCI6InRyaW5pdHkiLCJzaWQiOiJjZWU3YjYwYS02ZjAzLTQ2ZDgtYmJlMy1jMjFmYTBhMjI1ZjQiLCJzY29wZSI6Im9wZW5pZCB3ZWItb3JpZ2lucyBwcm9maWxlIGJhc2ljIHJvbGVzIG9wZW5pZC1jbGllbnQtc2NvcGUgZW1haWwgYWNyIiwicmV1c2VfaWQiOiI1NzNiMjc0MC0xZWRmLTQzOTUtYjZhYS02N2Q2MDY4MzNmMGYifQ.3Bh_OaBI9GqFkIa2TCxcHU-83NLe7p-x230cFYv8PZOv6bKN5TQfSu-aAtoXPP0E5yqaGmGLeOOK2hn92d9yWA'

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}


res = requests.get(f'{baseUrl}/uerp/v1/demo/device/cart', headers=headers, verify=False)
res.raise_for_status()
carts = res.json()

res = requests.get(f'{baseUrl}/uerp/v1/demo/operation/round', headers=headers, verify=False)
res.raise_for_status()
rounds = res.json()

for cart in carts:
    for round in rounds:
        if cart['roundId'] == round['id']:
            print(f'CART[{cart["name"]} : ROUND[{round["name"]}]')

for round in rounds:
    for cart in carts:
        if cart['id'] in round['cartIdList']:
            print(f'ROUND[{round["name"]}] : CART[{cart["name"]}]')