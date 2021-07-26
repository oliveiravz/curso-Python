from random import randint
from time import sleep

# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e 
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

num = int(input('Tente adivinhar qual número eu pensei entre 0 e 5: '))

print('\nPROCESSANDO...\n')
sleep(1)
if num < 0 or num > 5:
    print(f'{num}? Não é esse o nosso acordo!!')
else:
    sort = randint(0, 5)
    if num == sort:
        print(f'Eu pensei no {sort}: VOCÊ VENCEU!!')
    else:
        print(f'Eu pensei no {sort}: VOCÊ PERDEU!!')