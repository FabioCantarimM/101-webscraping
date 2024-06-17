import requests

url = "http://lumtest.com/myip.json"

# proxy = {
#     'http': 'http://localhost:8080',
#     'https': 'http://localhost:8080',
# }

headers = {
    "header": "content"
}


# Fazendo a requisição GET
# response = requests.get(url, proxies=proxy, verify=False, headers=headers)
# response = requests.get(url, proxies=proxy)
response = requests.get(url)
# Verifica se a requisição foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Imprime o conteúdo da resposta (o endereço IP retornado pelo site)
    print("Endereço IP retornado pelo site:", response.json())
    print("Cidade", response.json()["geo"] )
else:
    # Se a requisição não foi bem-sucedida, imprime o código de status
    print("Falha na requisição. Código de status:", response.status_code)
