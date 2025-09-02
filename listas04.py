# Programa para ler 10 números, preguiça de fazer até 20, inteiros e separar em listas de pares e ímpares

numeros = []
pares = []
impares = []

for numero in range(1, 21):
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Lista completa :D", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)
