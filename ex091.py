from random import randint
from time import sleep
from operator import itemgetter

# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. 
# No final, coloque esse dicionário em ordem, 
# sabendo que o vencedor tirou o maior número no dado.


print(f"{'[ENTER PARA JOGAR]':^30}")
play    = input()

jogadores = { 'jogador1': randint(1, 6),
              'jogador2': randint(1, 6),
              'jogador3': randint(1, 6),
              'jogador4': randint(1, 6)
            }
ranking = dict()
print('Valores sorteados: ')

for keys, values in jogadores.items() :
    print(f'{keys} tirou {values} no dado.')
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('=' * 30)
print('RANKING')
print('=' * 30)
for i, v in enumerate(ranking) :
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)

print('FIM!!')