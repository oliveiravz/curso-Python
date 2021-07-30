# Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
gols = list()
soma= 0

jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input('Qtde de Partidas: '))

for i in range(jogador['partidas']) :
    gols.append(int(input(f'Quantos gols o jogador fez na partida {i}: ')))
    soma += gols[i]
jogador['gols'] = gols[:]
jogador['total'] = soma

print('=' * 30) 
print(jogador)

print('=' * 30) 
for keys, values in jogador.items() :
    print(f'O campo {keys} tem o valor {values}')

print('=' * 30)
print(f"O jogador {jogador['nome']}, jogou {jogador['partidas']} partidas")
for i, values in enumerate(jogador['gols']) :
    print(f' => Na partida {i} fez {values}')
print(f"Foi um total de {jogador['total']} gols")