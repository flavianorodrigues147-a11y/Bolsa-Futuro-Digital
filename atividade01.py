# cálculo de sálario com descontos

valor1 = float(input('O valor recebido por hora trabalhada: '))
valor2 = float(input('A quantidade de horas trabalhadas no mês: '))
salario_bruto = valor1 * valor2


def calcular_salario_liquido(salario_bruto):
    inss = salario_bruto * 0.09
    ir = salario_bruto * 0.11
    sindicato = salario_bruto * 0.04
    return inss, ir, sindicato


inss, ir, sindicato = calcular_salario_liquido(salario_bruto)
print('O salário bruto é:', salario_bruto)
print('O desconto do INSS é:', inss)
print('O desconto do IR é:', ir)
print('O desconto do sindicato é:', sindicato)
print('Os descontos são:', inss + ir + sindicato)
descontos = inss + ir + sindicato

Saláriolíquido = salario_bruto - descontos
print('o salário liquido é:', Saláriolíquido)
