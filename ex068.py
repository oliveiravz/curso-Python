from random import randint

# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

soma = 0
par = impar = venceu = False
print('-' * 20, 'PAR OU IMPAR', '-' * 20)

while True :
    numero = int(input('Escolha um número: '))
    opcao = str(input('Par ou Ímpar [P/I]: ')).upper()

    while opcao not in 'PI' :
        opcao = str(input('Opção inválida! Tente Novamente: '))

    computador = randint(1, 10)
    total = computador + numero

    print(f'Você jogou {numero} e o computador jogou {computador}. Total de {total}', end='')

    if opcao == 'P' :
        if total % 2 == 0 :
            print(' Deu PAR')
            (print('VOCÊ VENCEU!!'))
        else :
            print(' deu ÍMPAR')
            break

    if opcao == 'I' :
        if total % 2 == 1 :
            print(' Deu ÍMPAR')
            print('VOCÊ VENCEU!!')
        else :
            print(' Deu PAR')
            break
    print('Vamos Jogar Novamente...')
print('Game Over!! Boa sorte na próxima.')


