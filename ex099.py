from random import randint
from time import sleep

# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* num) :
    print('Analisando os valores passados...')

    cont = maior = 0
    for numero in num :
        print(f'{numero}', end=' ', flush=True)
        sleep(0.3)

        if cont == 0 :
            maior = numero
        else :
            if numero > maior :
                maior = numero
        cont += 1
    print(f'\nForam digitados {cont} números ao todo!')
    print(f'\nO maior número é: {maior}')
    
maior(2, 9, 7, 8, 9)
maior(2, 1, 4)   