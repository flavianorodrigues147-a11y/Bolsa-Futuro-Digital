# tabuada com while
num = int(input("Digite o número para ver a tabuada: "))
n = 1
while n <= 10:
    resultado = num * n
    print(f"{num} x {n} = {resultado}")
    n += 1
