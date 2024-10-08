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
baseUrl = 'https://trinity.dev.local'
token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJkOHlPemhaSkJHU0ZUU3FBY2ZEYmpCM0pzOXpXSjFRRGJtTEhKclVEWVpRIn0.eyJleHAiOjE3MjQxNDk4OTgsImlhdCI6MTcyNDE0ODA5OCwiYXV0aF90aW1lIjoxNzI0MTQ4MDk4LCJqdGkiOiIyOWE5Y2YxZi03ODA4LTRkMmUtOTYwOS0wOThlMWMxYzQxZjYiLCJpc3MiOiJodHRwczovL3RyaW5pdHkuZXFwbHMubmV0L2F1dGgvcmVhbG1zL3RyaW5pdHkiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiYjZhNDM1NTgtNTU5MC00ODliLTg3ZWItZTNkNWUxY2JiYjFjIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoidHJpbml0eSIsInNpZCI6ImE2OTU0OGViLWY0ZDAtNDE5Ni1iYzE0LTJiNDA2ZGE1NjNhZSIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsib2ZmbGluZV9hY2Nlc3MiLCJkZWZhdWx0LXJvbGVzLXRyaW5pdHkiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgb3BlbmlkLWNsaWVudC1zY29wZSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwibmFtZSI6ImFkbWluIGFkbWluIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWRtaW4iLCJnaXZlbl9uYW1lIjoiYWRtaW4iLCJmYW1pbHlfbmFtZSI6ImFkbWluIiwiZW1haWwiOiJhZG1pbkB0cmluaXR5LmVxcGxzLm5ldCIsInBvbGljeSI6WyJhZG1pbiIsInVzZXIiXX0.enfetsSgEk5BUPn6ofaMyQMB3CNts3BiHV9kegpYsAqlhY93jteIvRqiEXbSD5Q0mAL9wRrYiN1VzIB6TWDrZV2XKHKu3W6-6r5963IC-10iyxNAZ_4zqHTQojWH7ydEllCBFJ1N1TciZXGR9Thr9rc3Zr0fkSsEjjJXwREjcsMX-vJzh_XsUppj4ICyll5cvR_a2kcTneX5PVLcHiSzqoAvnySI9rGJkP8boHUaxOVI7mAHA61p-GF5hfj19_FrB2NLZs51B3k9D6inrfrNBo6uOElDiCFBLJ9S8IjgqM_Xg5UHAygVBNPlStRp9TBS3rDljY_kSMUs73jHDupK0g'

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