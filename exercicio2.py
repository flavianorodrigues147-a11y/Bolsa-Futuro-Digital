numeros = [1, 2, 3, 2, 4, 2, 5]
quantidade_de_2 = numeros.count(2)
print("O número 2 aparece", quantidade_de_2, "vezes na lista.")

# Dada a lista idades = [12, 18, 25, 14, 30], use um laço para exibir somente as idades maiores ou iguais a 18.

idades = [12, 18, 25, 14, 30]
print(idades)
for idade in idades:
    if idade >= 18:
        print(
            f'As idades maiores que são igual ou maiores que 18 na lista são; {idade}')
    else:
        print(f'as idades que não são maiores ou igual a 18; {idade}')


# Crie uma lista valores = [10, 20, 30, 40]. Use um laço for para calcular manualmente a soma de todos os valores.

valores = [10, 20, 30, 40]
soma = 0

for valor in valores:
    soma += valor

print(f"A soma dos valores é: {soma}")


# Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas.
notas = []

aluno1 = float(input('Digite a primeira nota do aluno 1;'))
aluno1 = float(input('Digite a segunda nota do aluno 1;'))
aluno1 = float(input('Digite a terceira nota do aluno 1;'))
notas.append([aluno1, aluno1, aluno1])

aluno2 = float(input('Digite a primeira nota do aluno 2;'))
aluno2 = float(input('Digite a segunda nota do aluno 2;'))
aluno2 = float(input('Digite a terceira nota do aluno 2;'))
notas.append([aluno2, aluno2, aluno2])

media1 = (aluno1 + aluno1 + aluno1) / 3
media2 = (aluno2 + aluno2 + aluno2) / 3

print(f"Média do aluno 1: {media1:}")
print(f"Média do aluno 2: {media2:}")
