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
token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJzajE1bWhpcHlUNTJJM1N6dWFGZDRRMzFfeUx1OUZzRFFWeUFfcXQ2cERJIn0.eyJleHAiOjE3MjM5NjA0MDIsImlhdCI6MTcyMzk1ODYwMiwiYXV0aF90aW1lIjoxNzIzOTU4NjAyLCJqdGkiOiJiMjUzN2QzMS1lMzJmLTQ0NTktYTY4NC1jYzEzMjY5MjQyMjQiLCJpc3MiOiJodHRwczovL3RyaW5pdHkuZXFwbHMubmV0L2F1dGgvcmVhbG1zL3RyaW5pdHkiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiMTBlZjkyN2QtZDcxNy00NjFmLTg2OWMtNmVkNmI1ZGU0MmRiIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoidHJpbml0eSIsInNpZCI6ImQ0MmY1ODUzLWRiN2QtNDc5OS05Nzg2LWMzOWJhYTJlNTM3NCIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJkZWZhdWx0LXJvbGVzLXRyaW5pdHkiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIG9wZW5pZC1jbGllbnQtc2NvcGUgZW1haWwgcHJvZmlsZSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwibmFtZSI6ImFkbWluIGFkbWluIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWRtaW4iLCJnaXZlbl9uYW1lIjoiYWRtaW4iLCJmYW1pbHlfbmFtZSI6ImFkbWluIiwiZW1haWwiOiJhZG1pbkB0cmluaXR5LmVxcGxzLm5ldCIsInBvbGljeSI6WyJhZG1pbiIsInVzZXIiXX0.gHjIuHBcTMP86CDfxUpgvisjlyO35iCFu9PWKc0yfmb27XVJymtk1Wraqn4jKmdfY57jnR4rTMjFVQsslR14wi6qm4AqU4q9URAJNT-qSqm98GNa5fTrdr-qHTZUDfJKcT4h_D_Tc1VU_JmXsateiuNYhlYEfPs_D0syg8PPnGtKrs7VebW0EeQqIQExZccBLp4HitXIfWzvcXDQJgHYZH8SsODjQxvmoUEjbRGfQpmSfFOO3fBAxSJXyjjCPdcUDtnlUdn0_BOuREQWFQ7goCOpAbFzlO5MPQifz4cnsXubBcD3U-2JXPriCFi6hldm6MuNsimdLkTQzbxoieXKDw'

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