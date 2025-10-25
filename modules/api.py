import os
import requests

def conexao_api(cidade):
    chave_api = os.getenv("KEY_API")

    if not chave_api:
        print("Erro: Chave da API não encontrada. Verifique o arquivo .env.")
        return

    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {
        'q': cidade,
        'appid': chave_api,
        'units': 'metric',
        'lang': 'pt_br'
    }

    resposta = requests.get(url, params=params)

    if resposta.status_code == 200:
        print('\nAPI carregada com sucesso.\n')
        return resposta.json()
    else:
        print(f'Erro: {resposta.status_code} na API.')
        return
