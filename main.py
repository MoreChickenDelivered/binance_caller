from utils import Subexchange, signed_get_request

api_key = ''
secret_key = ''
subexchange = Subexchange.SPOT
endpoint = '/sapi/v1/margin/account'

def main():
    response  = signed_get_request(subexchange, endpoint, api_key, secret_key)
    print(f'Code: {response.status_code}')
    print(f'Response: {response.text}')

if __name__ == '__main__':
    main()