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
token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJreXdzeEVrc3ZWT296RDR4dmZlY2I0amF3R2tyYTlicm5hU1Y4cHNMdFdvIn0.eyJleHAiOjE3MjQyMjU0MjEsImlhdCI6MTcyNDIyMzYyMSwiYXV0aF90aW1lIjoxNzI0MjIzNjIxLCJqdGkiOiIwZmE2MzU0Yi1iY2RkLTRhZGQtODU0MC0wNmJlOTI2M2M5NGYiLCJpc3MiOiJodHRwczovL3RyaW5pdHkuZXFwbHMubmV0L2F1dGgvcmVhbG1zL3RyaW5pdHkiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiZjZiOGVhZjEtZTkxZi00MjZiLTlkNzctZmE5YmYzMzE0YTk5IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoidHJpbml0eSIsInNpZCI6IjJjNjZiNzZhLTZmNzEtNGY0Mi1hNjM5LTc1MTk5MTU0NzhhNiIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJkZWZhdWx0LXJvbGVzLXRyaW5pdHkiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgb3BlbmlkLWNsaWVudC1zY29wZSBlbWFpbCIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwibmFtZSI6ImFkbWluIGFkbWluIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWRtaW4iLCJnaXZlbl9uYW1lIjoiYWRtaW4iLCJmYW1pbHlfbmFtZSI6ImFkbWluIiwiZW1haWwiOiJhZG1pbkB0cmluaXR5LmVxcGxzLm5ldCIsInBvbGljeSI6WyJhZG1pbiIsInVzZXIiXX0.CBnGJ3TIT6Zcgzxd0tNMwYsnJuWJg6GjlZqNbIo91AyNuPEakqzCbrrLoCJ4hBmd2M_5Vr3520EdMszsWsrublceYFtRCSGNrfYGQGfBlxFiseonIjeD4wqy0jgFHG-roGpchM-jQAaWWQXuL7CwxL5JEJXWfMzEEVz3zfAP3lWUeq-7JHm5gDixVKApEF-MP8ts_N0cJ-UpwGYQwewFZ2aN0U5Klp0CX6yq83nlVa8WRt3vlwAn7VUV1li9mMCHOvRNsHzph6y1myyUWO78YFbK3XVFmPFZ8k3KzVRNhkj8eA54grE6BvRe6mLfV_3oHsHKtx0YkXnx1G5xnQetRQ'

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

# insert()
# time.sleep(3)
# mapping()

remove()


