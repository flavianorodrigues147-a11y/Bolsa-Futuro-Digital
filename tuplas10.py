num = int(input("Digite um número: "))
pares = [num for num in range(1, num + 1) if num % 2 == 0]
print("Números pares de 1 até", num, ":", pares)
