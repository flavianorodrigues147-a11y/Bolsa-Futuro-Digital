# Faça um Programa que leia e armazene 50 números inteiros, mostre a soma, a multiplicação e os números.

numeros = []
soma = 1
multiplicacao = 1

for numero in range(1, 51):
    numeros.append(numero)
    soma += numero
    multiplicacao *= numero

print(f"os numeros da lista: {numeros}")
print(f"A soma dos numeros: {soma}")
print(f"a mutiplicacao dos numeoros: {multiplicacao}")
