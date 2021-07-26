from random import randint

# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

maior = menor = valor = 0
lista = []

for i in range(5) :
    lista.append(randint(0, 10))
    if i == 0 :
        maior = menor = lista[i]
    else :
        if maior < lista[i] :
            maior = lista[i]
        if menor > lista[i] :
            menor = lista[i]

print(f'Lista: {lista}')
for pos, valor in enumerate(lista) :
    if valor == maior :
        print(f'O maior número: {maior} na posição {pos}')
    else :
        if valor == menor :
            print(f'O menor número: {menor} na posicao {pos}')