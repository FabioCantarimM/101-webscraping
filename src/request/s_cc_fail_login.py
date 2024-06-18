import requests
import os
from bs4 import BeautifulSoup

# Iniciar uma sessão
with requests.Session() as s:
    # URL do site
    url = 'https://www.codechef.com'
    login_url = 'https://www.codechef.com/api/codechef/login'
    dashboard_url = 'https://www.codechef.com/api/learn/dashboard'

    # Definir os dados de login
    payload = {
        'name': os.getenv('CC_USER'),
        'pass': os.getenv('CC_PASS'),
        'form_build_id': 'form-x2l2KziYvExzt1PijkFSUOClv090dJWthuVUlVYl2LM',
        'form_id': 'ajax_login_form'
    }

    # Fazer uma solicitação POST para o endpoint de login
    login = s.post(url=login_url, data=payload)

    if login.status_code == 200:
        print("Login bem-sucedido")
        dashboard = s.get(url=dashboard_url)
        if dashboard.status_code == 200:
            print(f'Sucesso ao receber os dados de Dashboard: Status Code - {dashboard.status_code}')
            print(dashboard.text)
        else:
            print(f'Falha ao receber os dados de Dashboard: Status Code - {dashboard.status_code}')
    else:
        print("Falha no login")
        print(login.status_code)
        print(login.text)
