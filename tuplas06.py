numeros = []
for i in range(5):
    num = float(input(f"Digite o número: "))
    numeros.append(num)

soma_total = sum(numeros)
print(f"A soma total dos números é: {soma_total}")
