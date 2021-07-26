# Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.


print('=' * 20)
print('CADASTRE UMA PESSOA')
print('=' * 20)
op = ''
contM = contI = contF = 0
while True :
    sexo = str(input('Digite o sexo [F/M]: ')).upper()
    while sexo not in 'FM' :
        sexo = str(input('Dado inválido! Tente novamente [F/M]: '))
    
    idade = int(input('Digite a idade: '))

    op = str(input('Deseja continuar? [S/N]: ')).upper()
    while op not in 'SN' :
        op = str('Opção inválida! Tente novmamente: ')
    
    if idade < 18 :
        contI += 1
    if sexo == 'M' :
        contM += 1
    if sexo == 'F' and idade < 20 :
        contF += 1 

    if op == 'N' :
        break
print('=' * 20)
print(f'Pessoas com mais de 18 anos: {contI}')
print(f'Homens cadastrados: {contM}')
print(f'Mulheres com menos de 20 anos: {contF}')


