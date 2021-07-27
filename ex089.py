# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

boletim = list()

while True : 
    nome  = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    boletim.append([nome, [nota1, nota2], media])

    opcao = str(input('Quer continuar?: '))
    if opcao in 'Nn' : 
        break

print('=' * 30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('-' * 30)
for i, b in enumerate(boletim) :
    print(f'{i:<4}{b[0]:<10}{b[2]:>8.1f}')

while True :
    print('-' * 35)
    flag = int(input('Mostrar notas de qual aluno?: '))
    if flag == 999 :
        break
    if flag <= len(boletim) - 1 :
        print(f'Notas de {boletim[flag][0]} são {boletim[flag][1]}')