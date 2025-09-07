idades = []
alturas = []


for i in range(10):
    print("Pessoa", i + 1)
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura (em metros): "))

    idades.append(idade)
    alturas.append(altura)


maior_altura = max(alturas)
indice = alturas.index(maior_altura)
print("A maior altura foi: ", maior_altura)
print("A idade mais alta foi: ", idades[indice])
