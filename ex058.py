from random import randint
from time import sleep

# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

sort = randint(1, 5)
cont = 1
while True :
    num = int(input('Tente adivinhar qual número eu pensei entre 1 e 5: '))
    
    if num != sort :
        num = int(input('Número errado/inválido! Tente novamente: '))
        cont += 1

    if num == sort :
        print(f'Pensei no {sort}, Parabéns você acertou em {cont} tentativas!! ')
        break 