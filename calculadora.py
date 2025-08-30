# calculadora
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input(f"Digite a operação (+, -, *, /): ")
if operacao == "+":
    resultado = num1 + num2
    print("Resultado da soma:", resultado)
elif operacao == "-":
    resultado = num1 - num2
    print("Resultado da subtração:", resultado)
elif operacao == "*":
    resultado = num1 * num2
    print("Resultado da multiplicação:", resultado)
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado da divisão:", resultado)
    else:
        print("Erro: Divisão por zero não é permitida.")
