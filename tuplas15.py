numeros = (2, 4, 6, 8, 10, 12, 14)

num = int(input("Digite um número para verificar: "))

if num in numeros:
    print(f"O número {num} está na tupla.")
else:
    print(f"O número {num} não está na tupla.")
