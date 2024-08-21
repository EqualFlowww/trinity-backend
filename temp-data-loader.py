# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
import json
import time
import requests

#===============================================================================
# Implement
#===============================================================================
baseUrl = 'https://trinity.eqpls.net'
token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJreXdzeEVrc3ZWT296RDR4dmZlY2I0amF3R2tyYTlicm5hU1Y4cHNMdFdvIn0.eyJleHAiOjE3MjQyMjM1ODksImlhdCI6MTcyNDIyMTc4OSwiYXV0aF90aW1lIjoxNzI0MjIxNzg5LCJqdGkiOiI3MDcxNmM3NS01ZjE2LTRlZmYtYmQ2ZC0wODUzZjA0ZGYxNTgiLCJpc3MiOiJodHRwczovL3RyaW5pdHkuZXFwbHMubmV0L2F1dGgvcmVhbG1zL3RyaW5pdHkiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiZjZiOGVhZjEtZTkxZi00MjZiLTlkNzctZmE5YmYzMzE0YTk5IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoidHJpbml0eSIsInNpZCI6ImE5MDEwYzUyLTAxNTgtNDczMi05OGZkLTZmNDEzNzIwZmQ0NCIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJkZWZhdWx0LXJvbGVzLXRyaW5pdHkiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgb3BlbmlkLWNsaWVudC1zY29wZSBlbWFpbCIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwibmFtZSI6ImFkbWluIGFkbWluIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWRtaW4iLCJnaXZlbl9uYW1lIjoiYWRtaW4iLCJmYW1pbHlfbmFtZSI6ImFkbWluIiwiZW1haWwiOiJhZG1pbkB0cmluaXR5LmVxcGxzLm5ldCIsInBvbGljeSI6WyJhZG1pbiIsInVzZXIiXX0.IDg5BQVAMbTW4XUsgYBYAbf2Mj_xtozD-gYI6R3vLifJn5cTbqNu2AedrEB33c52A15GAJ-HZE7ySa163ytgwNj4oJ6mdqSUBAXvLA_pPmJKEK4xVcIfxvXeQJa5d_376FXX-TI6pLuVq4YbgPQZwqM0p-PBL5RX6MPNa6xocA8J9heYo5ivp9ZfFMhEmoWw3SlKvwnBQaTNqAkf748SdRwwApVIQCWo3IGMkkTVJE8zwUINkAmq_-OX2fm0ZTkSRnWjQj26aHnRTbKfChH4ufd8xYAvMXgHh1Jd_rthCicONZmN8IWpxIpKftzM91xgGdrn2YFZK-EJSSz2SaDl0w'

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

insert()
time.sleep(3)
mapping()
# remove()


