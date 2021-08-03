# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los 
# dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def sorteia(lista) :
    print('Sorteando números da lista', end=' ')
    for cont in range(5) :
        lista.append(randint(1, 10))

def somaPar(par) :
    soma = 0
    for cont in range(5) :
        if par[cont] % 2 == 0 :
            soma += par[cont]
        print(f'A soma dos números pares: {soma}')

numeros = list()
sorteia(numeros)
print(numeros)
somaPar(numeros)