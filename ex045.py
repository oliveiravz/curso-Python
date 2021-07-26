from random import randint
from time import sleep
from termcolor import colored

# Crie um programa que faça o computador jogar Jokenpô com você.

s = 1

while s == 1 :
    print('=' * 30)
    print('||', end=' ')
    print(colored('PEDRA, PAPEL OU TESOURA', 'yellow'), end=' ')
    print('||')
    print('=' * 30)
    opcao = int(input('1 - Pedra\n2 - Papel\n3 - Tesoura\n\nESCOLHA: '))

    while opcao not in range(1, 4) :
        print(colored('Opção inválida! Tente novamente', 'red'))
        opcao = int(input('ESCOLHA: '))
    else :

        jokenpo = randint(1, 3)
        print(colored('\nJO...', 'yellow'))
        sleep(1)
        print(colored('KEN...', 'yellow'))
        sleep(1)
        print(colored('PÔ!!\n', 'yellow'))

        if jokenpo == 1 and opcao == 1 or jokenpo == 2 and opcao == 2 or jokenpo == 3 and opcao == 3 :
            print('Empate')
        elif jokenpo == 1 and opcao == 3 :
            print('PC: PEDRA\nVocê: TESOURA')
            print(colored('\nPERDEU', 'red'))
        elif jokenpo == 3 and opcao == 1 :
            print('PC: TESOURA\nVocê: PEDRA')
            print(colored('\nGANHOU', 'green'))
        elif jokenpo == 2 and opcao == 1 :
            print('PC: PAPEL\nVocê: PEDRA')
            print(colored('\nPERDEU', 'red'))
        elif jokenpo == 1 and opcao == 2 :
            print('PC: PEDRA\nVOCÊ: PAPEL')
            print(colored('\nGANHOU', 'green'))
        elif jokenpo == 3 and opcao == 2 :
            print('PC: TESOURA\nVocê: PAPEL')
            print(colored('\nPERDEU', 'red'))
        elif jokenpo == 2 and opcao == 3 :
            print('PC: PAPEL\nVocê: TESOURA')
            print(colored('\nGANHOU', 'green'))

    s = int(input('Jogar novamente? 1 = sim | 0 = Não: '))

    while s != 0 and s != 1 :
        print(colored('Opção inválida! Tente novamente', 'red'))
        s = int(input('Jogar novamente? 1 = sim | 0 = Não: '))
    