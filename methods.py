import json
import requests

url = 'http://127.0.0.1:8080/api-loja/produtos'


def adiciona_dados(data, url):
    dado_json = json.dumps(data)
    r = requests.post(url, data=dado_json, headers={'content-type': 'application/json'})
    return print(r.text)


def altera_dados(data, url):
    dado_json = json.dumps(data)
    r = requests.put(url, data=dado_json, headers={'content-type': 'application/json'})
    return print(r.text)


def ler_dados(dados, url):
    dado_json = json.dumps(dados)
    r = requests.get(url, data=dado_json, headers={'content-type': 'application/json'})
    return print(r.text)


def delete_dados(dados, url):
    dado_json = json.dumps(dados)
    r = requests.delete(url, data=dado_json, headers={'content-type': 'application/json'})
    return print(r.text)


adiciona_dados({'descricao': 'shampoo', 'ganhopercentual': '10'}, url)
adiciona_dados({'descricao': 'Condicionador', 'ganhopercentual': '20'}, url)
adiciona_dados({'descricao': 'Hidratante', 'ganhopercentual': '30'}, url)

altera_dados({'descricao': 'Dados modificados', 'ganhopercentual': '40', 'idproduto': '4'}, url)
altera_dados({'descricao': 'Dados modificados2', 'ganhopercentual': '50', 'idproduto': '5'}, url)

ler_dados({'idproduto': '1'}, url)
ler_dados({'idproduto': '2'}, url)

delete_dados({'idproduto': '1'}, url)
delete_dados({'idproduto': '2'}, url)




