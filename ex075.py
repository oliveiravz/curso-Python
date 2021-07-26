# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = (int(input('1º número: ')), int(input('2º número: ')), int(input('3º número: ')), int(input('4º número: ')))
print(num)
print(f'O número 9 aparece {num.count(9)}')

if 3 in num :
    print(f'O número 3 aparece na posicão {num.index(3)}')
else :
    print('O número 3 não foi digitado')

for i in num :
    if i % 2 == 0 :
        print(f'{i} é um número par')