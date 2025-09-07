# Lendo a lista A com 10 números inteiros
A = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    A.append(num)
# Calculando a soma dos quadrados
soma_quadrados = 0
for num in A:
    soma_quadrados += num ** 2
# Mostrando o resultado
print("A soma dos quadrados dos elementos é:", soma_quadrados)
