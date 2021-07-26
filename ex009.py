# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número: '))

print('='*15)
for i in range(1, 11):
    tab = n * i
    print('{} x {:2} = {}'.format(n, i, tab))
print('='*15)