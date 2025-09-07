# Link: https://docs.google.com/document/d/1AJugvPUcHAv_vJtWDHWuNUeiH7bJWXPSsp6W1xwRi9Y/edit?usp=drivesdk da atividade.


livros = ['As Crônicas de Gelo e Fogo',
          'As Crônicas de Nárnia', 'Imortal Kalymor']

primeiro_elemento = livros[0]
ultimo_elemento = livros[-1]

print(f"Primeiro elemente: {primeiro_elemento}")
print(f"Ultimo elemento da lista: {ultimo_elemento}")


# Adicione mais dois livros à lista livros usando o método append() e exiba a lista atualizada.
livros.append('Pequeno Princípe')
livros.append('Lovecraft')
print(livros)
# Insira o livro "Duna" na segunda posição da lista livros usando insert().
livros.insert(1, 'Duna')
print(livros)


# Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado".
livro1 = "Silêncio dos inocentes"
if livro1 in livros:
    livros.remove('livro')
    print('O livro está na lista.')
else:
    print('O livro não está na lista.')

# Percorra a lista livros e exiba cada livro com a frase: "O livro <nome do livro> é interessante"


for livro in livros:
    print(f'O livro {livro} é interessante.')
