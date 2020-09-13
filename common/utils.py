from settings import *
import requests

def get_token(institution):
    '''
    Responsável por conectar-se nas APIs do Open Banking e realizar a autenticação, retornando o token JWT de autorização
    '''
    
    url_token = API_BANKS[institution]['URL_TOKEN']
    api_key_authorization = API_BANKS[institution]['API_KEY']

    headers = {
        'authorization': 'Basic ' + str(api_key_authorization, "utf-8"),
        'cache-control': 'no-cache',
        'content-type' : 'application/x-www-form-urlencoded'
    }
    body = {   
        'grant_type': 'client_credentials',
        'scope' : 'urn:opc:resource:consumer::all'
    }
    
    response = requests.post(url= url_token, headers=headers, data=body)    
    auth_token = response.json()['access_token']
    
    return auth_token

def get_account_data(institution, account, token):
    '''
    Responsável por extrair os dados de uma determinada conta das apis do open banking
    '''
    url_institution_api = API_BANKS[institution]['URL']
    url_transactions = API_BANKS[institution]['URL_EXTRACT'].format(account)

    headers = {
        'authorization': 'Bearer ' + token       
    }
    body = {   
        
    }
    response = requests.get(url= url_institution_api + url_transactions, headers=headers, data=body)
    transaction_data = ''
    
    if response.status_code == 200:
        transaction_data = response.json()

    return transaction_data
