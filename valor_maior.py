# um programa que peça dois numeros e imprima o maior deles
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))


def imprimir_maior(num1, num2):
    if num1 > num2:
        print(f"O maior numero é: {num1}")
    elif num2 > num1:
        print(f"o maior numero é: {num2}")
    else:
        print("os dois sao iguais")


imprimir_maior(num1, num2)
