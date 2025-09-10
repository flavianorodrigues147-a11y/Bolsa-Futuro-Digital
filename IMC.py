def IMC():
    altura = float(input('Digite sua altura;'))
    peso = float(input('Digite seu peso;'))
    imc = peso/altura**2
    print(f'Seu IMC vai ser igual a; {imc: .2f}')


IMC()
