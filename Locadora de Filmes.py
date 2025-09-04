# menu da locadora de filmes

listar_filmes = ["Teen Wolf", "Dexter", "Guardiões da Galáxia",
                 "The 100", "You", "Thunderbolts"]  # filmes disponíveis


alugados = ["O Poderoso Chefão", "Clube da Luta",
            "A Origem", "Matrix", "O Rei Leão"]  # filmes alugados

escolha = 0
while escolha != 4:
    print("LOCADORA DE FILME ONLINE :D")
    print("1 - Listar filmes")
    print("2 - Devolver um filme")
    print("3 - Alugar um filme")
    print("4 - Sair")
    escolha = int(input("Digite uma opção:"))

    while True:

        if escolha == 1:
            print(listar_filmes)
            break
        elif escolha == 2:
            print(f"Filmes para serem devolvidos: {alugados}")
            nome_filme = input("Digite o nome do filme:")
            if nome_filme not in listar_filmes and nome_filme in alugados:
                alugados.remove(nome_filme)
                listar_filmes.append(nome_filme)
                print("Filme devolvido com sucesso!")
                break
            else:
                print("O filme digitado não está na lista!")
                break

        elif escolha == 3:
            print(listar_filmes)
            nome_filme = input("Digite o nome do filme:")
            if nome_filme in listar_filmes:
                listar_filmes.remove(nome_filme)
                alugados.append(nome_filme)
                print("Filme alugado com sucesso!")
            break

        elif escolha == 4:
            print("Porque você saiu? :(")
            break
