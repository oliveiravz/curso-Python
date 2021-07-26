# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. 
# No final, mostre:                                                                                                    
# A) Quantas pessoas foram cadastradas.                                                                                                                
# B) Uma listagem com as pessoas mais pesadas.                                                                                                    
# C) Uma listagem com as pessoas mais leves.

pessoas = list()
dado    = list()
pesado  = list()
leve    = list()
nomeP   = list()
nomeL   = list()
totalPessoas = 0

while True :
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso [Kg]: ')))
    if totalPessoas == 0 :
        pesado = leve = dado[1]
    else :
        if dado[1] > pesado :
            pesado = dado[1]
        if dado[1] < leve :
            leve   = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    totalPessoas += 1

    opcao = str(input('Quer continuar?: ')).upper()
    while opcao not in 'SN' :
        opcao = str(input('S para sim | N para não: ')).upper()
    
    if opcao == 'N' :
        print('=' * 30)
        print(f'Você cadastrou o total de {totalPessoas} pessoas')
        print(f'O maior peso é {pesado}Kg. Peso de ', end='')
        for p in pessoas :
            if p[1] == pesado :
                print(f'[{p[0]}]', end='')
        print(f'\nO menor peso é {leve}Kg. Peso de ', end='')
        for p in pessoas :
            if p[1] == leve :
                print(f'[{p[0]}]', end='')
        break


