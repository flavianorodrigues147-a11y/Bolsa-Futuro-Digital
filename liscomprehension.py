# Crie uma lista com os quadrados dos números de 1 a 20.

quadrados = [num ** 2 for num in range(1, 21)]
print(quadrados)

# Crie uma lista apenas com os números pares de 0 a 50.

lista = [num for num in range(1, 51) if num % 2 == 0]
print(f'Os numeros que são pares {lista}')

# Dada a string "comprehension", crie uma lista com apenas as vogais.

string = 'comprehension'
vogais = ['a', 'e', 'i', 'o', 'u']
lista_vogais = [letra for letra in string if letra in vogais]
print(f'As vogais são: {lista_vogais}')

# Gere uma lista de números múltiplos de 3 entre 0 e 30.

mutiplos = [num for num in range(1, 31) if num % 3 == 0]
print(mutiplos)

# Crie uma lista de tuplas (n, n²) para n de 1 a 10.

tuplas = [(num, num**2) for num in range(1, 11)]
print(tuplas)
