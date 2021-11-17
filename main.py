from utils import Subexchange, signed_get_request
import json

api_key = ''
secret_key = ''
subexchange = Subexchange.SPOT
endpoint = '/sapi/v1/margin/account'
# https://binance-docs.github.io/apidocs/spot/en/#query-cross-margin-account-details-user_data

def process_response(response:str):
    response = json.loads(response)
    response['userAssets'] = {
        assetInfo for assetInfo in response['userAssets']
            if float(assetInfo['netAsset']) != 0
    }

def main():
    response  = signed_get_request(subexchange, endpoint, api_key, secret_key)
    
    print(f'Code: {response.status_code}')
    print(f'Response: {process_response(response.text)}')

if __name__ == '__main__':
    main()