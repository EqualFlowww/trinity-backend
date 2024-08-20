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
token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJVbE5jRy1OUVNQNTVzZjRsczFYMWFRSENUY0RKVHh6UlFTbGNMR2tpeU9jIn0.eyJleHAiOjE3MjQxNDg3NDQsImlhdCI6MTcyNDE0Njk0NCwiYXV0aF90aW1lIjoxNzI0MTQ2OTQ0LCJqdGkiOiI5MjQ4NzE0YS1hMDYyLTRkZGQtOWEzZi0zZDVkNjRlNGI4NmIiLCJpc3MiOiJodHRwczovL3RyaW5pdHkuZXFwbHMubmV0L2F1dGgvcmVhbG1zL3RyaW5pdHkiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiYWVlNzE3NDQtNjlmZS00NTIwLTk4MTAtYjU1M2MzZDBjMjVhIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoidHJpbml0eSIsInNpZCI6ImNlZTdiNjBhLTZmMDMtNDZkOC1iYmUzLWMyMWZhMGEyMjVmNCIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJkZWZhdWx0LXJvbGVzLXRyaW5pdHkiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgb3BlbmlkLWNsaWVudC1zY29wZSBlbWFpbCIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwibmFtZSI6ImFkbWluIGFkbWluIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWRtaW4iLCJnaXZlbl9uYW1lIjoiYWRtaW4iLCJmYW1pbHlfbmFtZSI6ImFkbWluIiwiZW1haWwiOiJhZG1pbkB0cmluaXR5LmVxcGxzLm5ldCIsInBvbGljeSI6WyJhZG1pbiIsInVzZXIiXX0.Zx1uAeUti_B7GUCzcuwWhfPNW5HdG5yYWsIzi9yMp5IVtxcw3TNoRPKCJVPMTjF---NtLfpD47iWq3-MWqNOLBzCFx4seU_pdEgL-9r4To4MPd15AHgv_ZMYl7OtR8xrY60HODc7ldodCLOW6_V0Km4E-zd_q0SuIAMj7h_HhbOqpKpKxgXW2GIXHFeiGZ9l0mB245aSo_Lmv-DF-IMdgWsI2XFH2Y0XDyfF8uvXihDPxWk3ZV7sYeHR4WSIjxrITcNr-84iKHX07dEO8xUl0XyLg9Isdkc9qQlFfrnIPU2hqq9dFPTXik7eej7_cqtWffwg0_knV36J-wTJIRrOGg'

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