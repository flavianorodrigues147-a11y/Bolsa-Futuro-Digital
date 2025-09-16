import math 
#exemplo, aqui ele vai usar a biblioteca math para fazer o cálculo da raiz quadrada.
#se eu quiser usar a biblioteca math, eu preciso importar ela primeiro.
#se eu quiser usar uma função específica da biblioteca, eu preciso chamar ela com o nome da biblioteca + ponto + nome da função.
#exemplo:
print(math.sqrt(25))

#Uma biblioteca é um conjunto de funções, métodos e classes já prontas que você pode usar no seu código para evitar reinventar a roda. Elas ajudam a resolver problemas específicos — como cálculos matemáticos, manipulação de arquivos, criação de interfaces gráficas, entre outros.

#Existem bibliotecas padrão do Python, que já vêm instaladas com a linguagem, e bibliotecas de terceiros, que você pode instalar usando o gerenciador de pacotes pip.

import datetime
hoje = datetime.date.today()
print("Data de hoje:", hoje)
#A biblioteca datetime é usada para trabalhar com datas e horas. No exemplo acima, usamos a função date.today() para obter a data atual.

import random
print(random.randint(1, 10))  # Número aleatório entre 1 e 10
#A biblioteca random é usada para gerar números aleatórios. No exemplo acima, usamos a função randint() para gerar um número inteiro aleatório entre 1 e 10.

