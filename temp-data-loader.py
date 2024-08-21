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
token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJjT0tQMVExcFJnSTFRbGgxd29FSF9GdFhfQlNsWFdpUlp0MG9SMXJjeDFFIn0.eyJleHAiOjE3MjQyMjI5NjcsImlhdCI6MTcyNDIyMTE2NywiYXV0aF90aW1lIjoxNzI0MjIxMTE4LCJqdGkiOiJlYTQ3MDZlMS00ZDZmLTQ1ODYtOTllYy04NDFkYjI1MzEwODkiLCJpc3MiOiJodHRwczovL3RyaW5pdHkuZXFwbHMubmV0L2F1dGgvcmVhbG1zL3RyaW5pdHkiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiNmRmMWJhZDMtZDU0Mi00YzZmLWIxZmUtMDUyMWFkZGM0OGEwIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoidHJpbml0eSIsInNpZCI6ImZhZDFmNzc4LTdlZTgtNDVjNy1hZTEyLTdmOGIwNjRmZmFkYyIsImFjciI6IjAiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJkZWZhdWx0LXJvbGVzLXRyaW5pdHkiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIG9wZW5pZC1jbGllbnQtc2NvcGUgZW1haWwgcHJvZmlsZSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwibmFtZSI6ImFkbWluIGFkbWluIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWRtaW4iLCJnaXZlbl9uYW1lIjoiYWRtaW4iLCJmYW1pbHlfbmFtZSI6ImFkbWluIiwiZW1haWwiOiJhZG1pbkB0cmluaXR5LmVxcGxzLm5ldCIsInBvbGljeSI6WyJhZG1pbiIsInVzZXIiXX0.F6F2JSpEmG6YZnMAZNw_E5dvU0S31pZV5UaZHPZlvvUCrPsqapFbPczNAtdi27KmYhW23My9NYVHXaAmxtGBTISxYPwn2cn3t7GpJHGdoSOpzaJpOfansTDGQ1bQqsuVxaDKbcI_-9mTdvE7rcvxy-wdWvoP-bLPqXtm9gcCSChnaznZRG2OJvN2-7AveNp3aKnyGYwWbH70RSKJcIfsAL4UEpWwcAMASlGre12_xJlECkXz6KdyI2Y1yP8XP03823VRTpbqpw0yiBZZpXogjofv4n-eFImifGnPU7bTJNAME42SlsIsuSiKe9FTR9u3HHPI3lvhptKwmCN2LdT52w'

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
mapping()
# remove()


