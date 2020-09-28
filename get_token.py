import os
import sys
import json

sys.path.append(os.path.join(os.path.dirname(__file__), 'site-packages'))

import requests

API_URL = "http://localhost:18080/kabusapi"
API_PASSWORD = os.environ["API_PASSWORD"]

def get_token():  

    URL = API_URL + "/token"
    
    headers = {"content-type": "application/json"}
    payload = {"APIPassword": API_PASSWORD}

    try:
        response = requests.post(URL, data=json.dumps(payload).encode("utf8"), headers=headers)  
        token = json.loads(response.text).get("Token")

    except Exception as e:
        print (e)
    
    return token

def get_board(token):

    URL = API_URL + "/board/9433@1"
    headers = {
        "content-type": "application/json",
        "X-API-KEY": token
    }

    try:
        response = requests.get(URL, headers=headers)  
    except Exception as e:
        print (e)
    
    return json.loads(response.text)

print ("始めます")

token = get_token()

print (token)

res = get_board(token)

print (res)
