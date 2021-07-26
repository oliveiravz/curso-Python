# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

#  --> strip() remove os espaços de uma string
cidade = str(input('Informe o nome da sua cidade: ')).strip()
primeiro = cidade[:5].upper()

if primeiro == 'SANTO':
    print('Sua cidade se inicia com santo')
else:
    print('Sua cidade não se inicia com santo')