from datetime import date

# Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input('Informe o ano de seu nascimento: '))
anoAtual = date.today().year
dif = anoAtual - ano
alistamento = 18

if dif < alistamento :
    print(f'Você tem {dif} anos')
    print(f'Você deverá se alistar daqui {abs(dif - alistamento)} anos')
elif dif == alistamento :
    print(f'Você tem {dif} anos')
    print('Se aliste imediatamente!')
else :
    print(f'Você tem {dif} anos')
    print(f'Já passou o tempo do alistamento\nVocê deveria ter se alistado a {abs(dif - alistamento)} anos atrás')