escolha = 0  # Variável para armazenar a escolha do usuário no menu
contas = []  # Lista para armazenar todas as contas de usuários
conta_atual = None  # Variável para armazenar a conta atualmente acessada


def criar_conta():
    print("Criar Nova Conta")
    nome = input("Nome completo: ")
    cpf = input("CPF: ")
    usuario = input("Nome de usuário: ")
    senha = input("Senha: ")
    confirmar = input("Confirme a senha: ")

    if senha != confirmar:
        print("Erro: senhas não coincidem.")
        return criar_conta()

    else:
        print("Senha confirmada.")

        saldo = float(input("Saldo inicial: R$ "))

        conta = {
            "nome": nome,
            "cpf": cpf,
            "usuario": usuario,
            "senha": senha,
            "saldo": saldo,
            "historico": []
        }

        contas.append(conta)
        print("Conta criada com sucesso!")


def acessar_conta():
    print("Acessar Conta")
    usuario_conta = input("Nome de usuário da conta: ")
    senha_conta = input("Senha: ")

    for conta in contas:
        if conta["usuario"] == usuario_conta and conta["senha"] == senha_conta:
            print("Acesso concedido.")
            conta_atual = conta
            return conta_atual  # Retorna a conta atual para ser usada globalmente
        else:
            print("Erro: nome de usuário ou senha incorretos.")
            return None  # None significa que não há conta atual e precisa acessar uma conta


def ver_saldo():
    if conta_atual:
        # round para limitar a 2 casas decimais e o 2 é a quantidade de casas
        print("Saldo atual: R$", round(conta_atual["saldo"], 2))
    else:
        print("Você precisa acessar uma conta primeiro.")


def depositar():
    if conta_atual:
        valor = float(input("Valor para depositar: R$ "))
        if valor > 0:
            conta_atual["saldo"] += valor
            conta_atual["historico"].append(
                f"Depósito de R$ {round(valor, 2)}")
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido.")
    else:
        print("Você precisa acessar uma conta primeiro.")


def sacar():
    if conta_atual:
        valor = float(input("Valor para sacar: R$ "))
        if 0 < valor <= conta_atual["saldo"]:
            conta_atual["saldo"] -= valor
            conta_atual["historico"].append(f"Saque de R$ {round(valor, 2)}")
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")
    else:
        print("Você precisa acessar uma conta primeiro.")


def transferir():
    if conta_atual:
        destino_usuario = input("Usuário da conta de destino: ")
        valor = float(input("Valor para transferir: R$ "))
        if valor <= 0:
            print("Valor inválido.")
            return
        destino = None
        for conta in contas:
            if conta["usuario"] == destino_usuario:
                destino = conta
                break
        if destino:
            if valor <= conta_atual["saldo"]:
                conta_atual["saldo"] -= valor
                destino["saldo"] += valor
                conta_atual["historico"].append(
                    f"Transferência para {destino_usuario} de R$ {round(valor, 2)}")
                destino["historico"].append(
                    f"Transferência de {conta_atual['nome']} de R$ {round(valor, 2)}")
                print("Transferência realizada com sucesso.")
            else:
                print("Saldo insuficiente.")

        else:
            print("Conta de destino não encontrada.")
    else:
        print("Você precisa acessar uma conta primeiro.")


def historico():
    if conta_atual:
        print("Histórico de transações:")
        for h in conta_atual["historico"]:
            print(" -", h)
    else:
        print("Você precisa acessar uma conta primeiro.")


def atualizar_dados():
    if conta_atual:
        print("Atualizar Dados Cadastrais")
        print("1 - Nome")
        print("2 - CPF")
        print("3 - Usuário")
        print("4 - Senha")
        opc = int(input("Escolha uma opção: "))

        if opc == 1:
            conta_atual["nome"] = input("Novo nome: ")
            print("Nome atualizado com sucesso.")
        elif opc == 2:
            conta_atual["cpf"] = input("Novo CPF: ")
            print("CPF atualizado com sucesso.")
        elif opc == 3:
            conta_atual["usuario"] = input("Novo nome de usuário: ")
            print("Usuário atualizado com sucesso.")
        elif opc == 4:
            nova = input("Nova senha: ")
            confirmar = input("Confirme a nova senha: ")
            while nova != confirmar:
                print("As senhas não coincidem.")
                nova = input("Nova senha: ")
                confirmar = input("Confirme a nova senha: ")
                conta_atual["senha"] = nova
                print("Senha atualizada com sucesso.")
        else:
            print("Opção inválida.")


while escolha != 9:
    print("    Sistema Bancário.")
    print("1 - Criar conta de usuário")
    print("2 - Acessar conta de usuário")
    print("3 - Ver saldo")
    print("4 - Depositar dinheiro")
    print("5 - Sacar dinheiro")
    print("6 - Transferir dinheiro")
    print("7 - Histórico de transações")
    print("8 - Atualizar dados cadastrais")
    print("9 - Sair")
    escolha = int(input("Digite uma opção: "))

    if escolha == 1:
        criar_conta()
    elif escolha == 2:
        conta_atual = acessar_conta()
    elif escolha == 3:
        ver_saldo()
    elif escolha == 4:
        depositar()
    elif escolha == 5:
        sacar()
    elif escolha == 6:
        transferir()
    elif escolha == 7:
        historico()
    elif escolha == 8:
        atualizar_dados()
    elif escolha == 9:
        print("Saindo do sistema. Até logo!")
    else:
        print("Opção inválida.")

else:
    print("Você precisa acessar uma conta primeiro.")
