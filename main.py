from utils import Subexchange, signed_get_request

api_key = ''
secret_key = ''

def main():
    print(signed_get_request(Subexchange.SPOT, '/sapi/v1/margin/account', api_key, secret_key))

if __name__ == '__main__':
    main()