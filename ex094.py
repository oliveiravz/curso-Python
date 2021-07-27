# Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
soma= 0
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input('Qtde de Partidas: '))

for i in range(jogador['partidas']) :
    jogador['gols'] = int(input(f'Quantos gols fez na {i}º partida: '))
    jogador['total'] += jogador['gols']

for keys, values in jogador.items() :
    print(keys, values)