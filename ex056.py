# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, 
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

media = 0
maisVelho = 0
nomeMaisVelho = ''
menos20Anos = 0

for i in range(1, 5) :
    print('=' * 10,f'{i}º PESSOA', '=' * 10)
    nome  = input(f'Digite o nome da {i}º pessoa: ')
    idade = int(input(f'Digite a idade da {i}º pessoa: '))
    sexo  = input(f'Digite o sexo da {i}º pessoa [m - f]: ').lower()

    media += idade / i
    maisVelho = idade

    if sexo == 'm' :
        nomeMaisVelho = nome
    
    if sexo == 'f' :
        if idade < 20 :
            menos20Anos += 1

print(f'Média de idade do grupo: {media:.2f}')
print(f'Nome do homem mais velho: {nomeMaisVelho}')
print(f'Quantidade de mulheres com menos de 20 anos: {menos20Anos}')