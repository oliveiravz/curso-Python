# Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre: 
#  A) Quantas pessoas foram cadastradas
#  B) A média de idade 
#  C) Uma lista com as mulheres 
#  D) Uma lista de pessoas com idade acima da média

pessoas = dict()
dados = list()
soma = media = 0
nomeF = ''
opcao = ''
while True :
    pessoas['nome'] = str(input('Nome: '))
    while True :
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper()
        if pessoas['sexo'] in 'MF' :
            break
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    dados.append(pessoas.copy())

    while True :
        opcao = str(input('Continue?: ')).upper()
        if opcao in 'SN' :
            break
    if opcao == 'N' :
        break

# print(pessoas)

media = soma / len(dados)
print(f'A) Total de pessoas: {len(dados)}')
print(f'B) Média de idade: {media:.2f}')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in dados :
    if p['sexo'] == 'F' :
        print(f'[{p["nome"]}]',end=' ')
print()
print('Lista de pessoas acima da média: ')
for p in dados :
    if p['idade'] >= media :
        for keys, values in p.items() :
            print('D) ', f' {keys} = {values}; ', end='')
        print()
print('FIM!') 
