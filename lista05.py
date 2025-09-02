aprovados = 0

for aluno in range(10):
    notas = []
    for nota in range(4):
        nota = float(input("Digite a nota: "))
        notas.append(nota)
    media = sum(notas)/4
    if media >= 7.0:
        aprovados += 1

print("Alunos com média maior ou igual a 7.0:", aprovados)

# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
