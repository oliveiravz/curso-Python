# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
cont = 0

for c in range(1, num + 1) :
    if num % c == 0 :
        cont += 1

if cont == 2 :
    print(f'{num} é um número primo')
else :
    print(f'{num} não é um número primo')