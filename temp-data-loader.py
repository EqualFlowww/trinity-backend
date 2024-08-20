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


def remove():
    res = requests.get(f'{baseUrl}/uerp/v1/demo/device/cart', headers=headers, verify=False)
    res.raise_for_status()
    for cart in res.json():
        requests.delete(f'{baseUrl}/uerp/v1/demo/device/cart/{cart["id"]}', headers=headers, verify=False)

    res = requests.get(f'{baseUrl}/uerp/v1/demo/operation/round', headers=headers, verify=False)
    res.raise_for_status()
    for round in res.json():
        requests.delete(f'{baseUrl}/uerp/v1/demo/operation/round/{round["id"]}', headers=headers, verify=False)

def insert():
    with open('temp-data.json', 'rb') as fd:
        fileData = fd.read()

    jsonData = json.loads(fileData)

    for cart in jsonData['TMP_CART_SUMMARY_DATA_COLLECTION'].values():
        cart.pop('id')
        cart['roundId'] = ''
        requests.post(f'{baseUrl}/uerp/v1/demo/device/cart', headers=headers, json=cart, verify=False)

    for round in jsonData['TMP_ROUND_SUMMARY_DATA_COLLECTION'].values():
        round.pop('id')
        round['cartIdList'] = []
        requests.post(f'{baseUrl}/uerp/v1/demo/operation/round', headers=headers, json=round, verify=False)

def mapping():
    cartRound = [
        '123:1', '456:2', '789:3', '112:4', '135:5', '718:6', '191:7', '222:8', '333:9', '444:10'
    ]

    for cr in cartRound:
        cart, round = cr.split(':')
        print(cart, round)

        res = requests.get(f'{baseUrl}/uerp/v1/demo/device/cart?name="{cart}"', headers=headers, verify=False)
        res.raise_for_status()
        cart = res.json()[0]

        res = requests.get(f'{baseUrl}/uerp/v1/demo/operation/round?name="ROUND {round}"', headers=headers, verify=False)
        res.raise_for_status()
        round = res.json()[0]

        cart['roundId'] = round['id']
        round['cartIdList'].append(cart['id'])

        res = requests.put(f'{baseUrl}/uerp/v1/demo/device/cart/{cart["id"]}', headers=headers, json=cart, verify=False)
        res.raise_for_status()

        res = requests.put(f'{baseUrl}/uerp/v1/demo/operation/round/{round["id"]}', headers=headers, json=round, verify=False)
        res.raise_for_status()

# remove()
# insert()
mapping()

