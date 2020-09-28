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
    except Exception as e:
        print (e)
    
    return json.loads(response.text).get("Token")


def get_price(token):

    symbol = "9433"
    exchange = "1"	
    URL = API_URL + "/board/" + symbol + "@" + exchange

    headers = {
        "content-type": "application/json",
        "X-API-KEY": token
    }

    try:
        response = requests.get(URL, headers=headers) 
    except Exception as e:
        print (e)
    
    return json.loads(response.text).get("price")


token = get_token()
res = get_board(token)

print (res)
