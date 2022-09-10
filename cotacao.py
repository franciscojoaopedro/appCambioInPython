import requests

def pegar_cotacoes(codigo):
    try:
        requisicao=requests.get(f"https://economia.awesomeapi.com.br/json/last/USD-{codigo}")
        requisicao_data=requisicao.json()
        cotacao=requisicao_data[f'{codigo}AOA']['bid']
        return cotacao
    except:
        print("codigo invalido")
        return None