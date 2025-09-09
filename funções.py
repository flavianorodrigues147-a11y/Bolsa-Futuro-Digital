# Crie uma função que receba um número e retorne o seu quadrado.

def quadrado():
    num = int(input('Digite um número para ver o seu quadrado:'))
    print(num * 2)


quadrado()

# Crie uma função que receba dois números e retorne o maior deles.
numeros = []


def maior_numero():
    num = int(input('Digite o número:'))
    num2 = int(input('Digite o segundo número:'))
    numeros.append(num)
    numeros.append(num2)
    numero_maior = max(numeros)
    print(f'O maior número entre {num} e {num2} é igual a; {numero_maior}')


maior_numero()

# Crie uma função que receba uma lista de números e retorne a soma.

lista = []


def somar_numero():
    soma = 0
    for num in range(10):
        lista.append(num)
        soma += num
    print(f'A soma dos números da lista é igual a: {soma}')
    print(f'Lista: {lista}')


somar_numero()

# Crie uma função que mostre a tabuada de um número.


def mostrar_tabuada():
    numero = int(input('Digite o número:'))
    print(f'Tabuada do {numero}:')
    for i in range(1, 11):
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')


mostrar_tabuada()

# Use lambda para criar uma função que calcule o dobro de um número.


def calcular_dobro():
    num = int(input('Digite o número:'))
    print(num*2)


calcular_dobro()
