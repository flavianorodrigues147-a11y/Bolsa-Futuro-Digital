# Instale a biblioteca requests e faça uma requisição para o site (o site está na atividade que a professora Ana Paula passou).

# https://www.google.com. site da atividade

import requests
# get() faz a requisição para o site
requisicao = requests.get('https://www.google.com')
print(f'A requisição do site: {requisicao}')
