# Faça um Programa que leia 40 notas, mostre as notas e a média na tela.
numeros = []
for num in range(1, 41):
    numeros.append(num)
    media = sum(numeros) / len(numeros)
print("Media = %.2f" % (media))
