
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# B = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Lendo as duas listas
A = []
B = []
C = []


print("Digite os 10 elementos da primeira lista:")
for i in range(10):
    valor = int(input(f"Elemento {i+1}: "))
    A.append(valor)

print("\nDigite os 10 elementos da segunda lista:")
for i in range(10):
    valor = int(input(f"Elemento {i+1}: "))
    B.append(valor)

print("\nDigite os 10 elementos da terceira lista:")
for i in range(10):
    valor = int(input(f"Elemento {i+1}: "))
    C.append(valor)


# Gerando a lista intercalada
intercalada = []
for i in range(10):
    A.append(A[i])
    B.append(B[i])
    C.append(C[i])

# Exibindo o resultado
print("\nPrimeira lista:", A)
print("Segunda lista:", B)
print("Terceira lista:", C)
print("Lista intercalada:", intercalada)
