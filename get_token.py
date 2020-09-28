import os
import sys
import json

sys.path.append(os.path.join(os.path.dirname(__file__), 'site-packages'))

import requests

API_URL = "http://localhost:18080/kabusapi/token"
API_PASSWORD = os.environ["API_PASSWORD"]

def get_token():  
    
    headers = {"content-type": "application/json"}
    payload = {"APIPassword": API_PASSWORD}

    try:
        response = requests.post(API_URL, data=json.dumps(payload).encode("utf8"), headers=headers)  
        token = json.loads(response.text).get("Token")

    except Exception as e:
        print (e)
    
    

    return token


#print (API_PASSWORD)

print (get_token())