# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

print('=' * 10, 'SEQUENCIA FIBONACCI', '=' * 10)

n = int(input('Informe quantos elementos você quer: '))
f = 0
c = 0
t1 = 0
t2 = 1

while c <= n :
    f = t1 + t2
    print(f'{f} - ', end='')
    c += 1
    t1 = t2
    t2 = f
print('FIM!')
