# tuplas com cores

cores = ('vermelho', 'verde', 'azul', 'amarelo', 'roxo')

if 'azul' in cores:
    print("azul parte da tupla.")
else:
    print("o azul não parte da tupla.")

print(cores[2], cores[0])
cores.append('laransa')  # o erro está aqui
