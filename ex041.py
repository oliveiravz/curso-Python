from datetime import date

# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

ano = int(input('Informe o ano do nascimento do atleta: '))
atual = date.today().year
idade = atual - ano
while idade < 0 :
    print('Informe informe um ano válido!! Tente Novamente')
    idade = int(input('Informe a idade do atleta: '))

if idade <= 9 :
    print('Categoria : MIRIM')
elif idade <= 14 :
    print('Categoria: INFANTIL')
elif idade <= 19 :
    print('Categoria: JUNIOR') 
elif idade <= 20 :
    print('Categoria: SENIOR')
else : 
    print('Categoria: MASTER')

# if idade <= 9 :
#     print('Categoria : MIRIM')
# elif idade > 9 and idade <= 14 :
#     print('Categoria: INFANTIL')
# elif idade > 14 and idade <= 19 :
#     print('Categoria: JUNIOR') 
# elif idade > 19 and idade <= 20 :
#     print('Categoria: SENIOR')
# else : 
#     print('Categoria: MASTER')