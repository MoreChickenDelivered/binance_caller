import hashlib
import hmac
import base64
from enum import Enum
from datetime import datetime
import urllib
import requests

class Subexchange(Enum):
    SPOT = 1
    USDT = 2
    COIN = 3

def hmac_binance(secret_key, msg):
    binary = hmac.new(bytes(secret_key, 'UTF-8'), msg=bytes(msg,
                          'UTF-8'), digestmod=hashlib.sha256).digest()
    return base64.b16encode(binary).decode('UTF-8')

def generate_params(secret_key):
    params = {'timestamp': str(
                round(datetime.now().timestamp()*1e3)), 'recvWindow': '10000'}
    suffix = urllib.parse.urlencode(params)
    signature = hmac_binance(secret_key, suffix)
    params['signature'] = signature
    return params

def signed_get_request(subexchange: Subexchange, endpoint: str, api_key: str, secret_key: str):
    subexchange2baseurl = {
        Subexchange.COIN: 'https://dapi.binance.com',
        Subexchange.USDT: 'https://fapi.binance.com',
        Subexchange.SPOT: 'https://api.binance.com'
    }
    url = subexchange2baseurl[subexchange] + endpoint
    params = generate_params(secret_key)
    response = requests.request('GET', url, params=params, headers={
                                        'X-MBX-APIKEY': api_key})
    return response                                    
                                    

