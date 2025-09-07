# O que é List Comprehension?
# É uma forma compacta e elegante de criar listas em Python. Em vez de usar um for tradicional para adicionar elementos a uma lista, você pode fazer tudo em uma única linha.


# 1. Cria o tabuleiro vazio
tabuleiro = [['[ ]' for _ in range(8)] for _ in range(8)]

# 2. Define as peças
pecas = ['tor', 'cav', 'bis', 'rai', 'rei', 'bis', 'cav', 'tor']
peoes = ['pea'] * 8

# 3. Coloca as peças pretas
tabuleiro[0] = pecas
tabuleiro[1] = peoes

# 4. Coloca as peças brancas
tabuleiro[6] = peoes
tabuleiro[7] = pecas

# 5. Imprime o tabuleiro
for linha in tabuleiro:
    # join serve para juntar elementos de uma lista de strings em uma única string, usando um separador que você escolhe.
    print(' '.join(linha))
