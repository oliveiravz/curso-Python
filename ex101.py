from datetime import date

# Crie um programa que tenha uma função chamada voto() 
# que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto
# NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(idade) :
    global nascimento
    anoAtual = date.today().year

    idade = anoAtual - nascimento

    if idade < 18 :
        print(f'Com {idade} anos o VOTO é NEGADO')
    elif idade >= 18 and idade < 65 :
        print(f'Com {idade} anos o VOTO é OBRIGATÓRIO')
    elif idade >= 65 :
        print(f'Com {idade} o VOTO é OPCIONAL')

print('-' * 50)
nascimento = int(input('Ano de nascimento: '))
voto(nascimento)