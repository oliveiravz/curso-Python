# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.



maioridade = 0
menoridade = 0

for c in range (1, 8) :
    nome = input('Informe o nome: ')
    nasc = int(input('Informe o ano de nascimento: '))
    print('\n')

    anoAtual = 2021
    idade = anoAtual - nasc

    if idade >= 21 :
        maioridade += 1
    else :
        menoridade += 1 

print(f'Pessoas maiores de idade: {maioridade}\nNúmero de pessoas menores de idade: {menoridade}')