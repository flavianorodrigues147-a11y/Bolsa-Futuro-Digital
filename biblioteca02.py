#Crie uma lista de nomes e use random.choice() para escolher um vencedor.
#O nome da questão da atividade é copiado e deixado como comentário no início do arquivo.
import random
nomes = ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo']
vencedor = random.choice(nomes)
#choice() escolhe um item aleatório de uma lista.
print(f'O vencedor é: {vencedor}')
