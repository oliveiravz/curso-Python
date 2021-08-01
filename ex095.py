# Aprimore o desafio 93 para que ele funcione com vários jogadores, 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = dict()
dados = list()
gols = list()
soma = 0

while True: 
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantidade de partidas do {jogador["nome"]}: '))
    gols.clear()
    for i in range(jogador['partidas']) :
        gols.append(int(input(f' => Gols na {i+1}ª partida: ')))
        soma += gols[i]
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    dados.append(jogador.copy())

    opcao = str(input('Cadastrar outro jogador? [S/N]: ')).upper()
    if opcao == 'N' :
        break

print('=' * 50)
print('cod ', end='')
for i in jogador.keys() :
    print(f'{i:<15}', end='')
print()
print('=' * 50)
for chaves, valores in enumerate(dados) :
    print(f'{chaves:>3} ', end='')
    for k in valores.values() :
        print(f'{str(k):<15}', end='')
    print()
print('=' * 50)
while True: 
    busca = int(input('Mostrar dados de qual jogador [999 para parar]: '))
    if busca == 999 :
        break
    if busca >= len(dados) :
        print(f'Erro! Nao existe jogador {busca}')
    else :
        print(f' => Levantamento do jogador -> {dados[busca]["nome"]} ')
        for indice, gols in enumerate(dados[busca]['gols']) :
            print(f' => No jogo {indice + 1 } fez {gols}.')
print('FIM DO PROGRAMA!!')