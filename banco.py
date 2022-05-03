import json
import requests

dado = {'descricao':'alcatra','ganhopercentual': 9}
dado_json = json.dumps(dado)
url = 'http://127.0.0.1:8080/api-loja/produtos'
r = requests.post(url, data=dado_json, headers={'content-type': 'application/json'})
print(r.text)