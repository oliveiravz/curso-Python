from random import randint
from time import sleep

# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 
# para cada jogo, cadastrando tudo em uma lista composta.

numero = list()
jogos  = list()
cont = 1

print('=' * 30)
print(f"{'APOSTAS MEGASENA':^30}")
print('=' * 30)

qtde = int(input('Quantas apostas você quer?: '))

while cont <= qtde :
    for linha in range(6) :
        n = randint(1, 60)
        if n not in numero :
            numero.append(n)
    jogos.append(numero[:])
    numero.clear()
    cont += 1

print('=' * 3, f'Sorteando {qtde} jogos', '=' * 3)
for i, j in enumerate(jogos) :
    sleep(1)
    print(f'{i+1}º jogo - {sorted(j)}')
    
print('=' * 30)
print(f"{'Boa sorte':^30}")