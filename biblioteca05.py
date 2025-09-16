# Instale a biblioteca requests e faça uma requisição para o site (o site está na atividade que a professora Ana Paula passou).

# https://www.google.com. site da atividade

import requests
# get() faz a requisição para o site
requisicao = requests.get('https://www.google.com')
print(f'A requisição do site: {requisicao}')

# A biblioteca requests é uma biblioteca de terceiros que facilita fazer requisições HTTP em Python. Com ela, você pode enviar requisições GET, POST, PUT, DELETE, entre outras, para interagir com APIs e obter dados da web.

#O método get() é usado para fazer uma requisição GET, que é o tipo mais comum de requisição HTTP. Ele retorna um objeto de resposta que contém informações sobre a resposta do servidor, como o status da requisição, os cabeçalhos e o conteúdo da resposta.

#O print acima mostra o status da requisição. Se o status for 200, significa que a requisição foi bem-sucedida e o servidor retornou a página solicitada. Outros códigos de status comuns incluem 404 (página não encontrada) e 500 (erro interno do servidor).

#Flaviano


