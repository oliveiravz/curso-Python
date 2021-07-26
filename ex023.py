# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Informe um número entre 0 e 9999: '))
# num = int(input('Informe um número entre 0 e 9999: '))
# split() --> separa as palavras de uma string
# n = num.split()

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Milhar: {m}\nCentena: {c}\nDezena: {d}\nUnidade: {u}')

# print(f'Unidade: {num[3]}')
# print(f'Dezena:  {num[2]}')
# print(f'Centena: {num[1]}')
# print(f'Milhar:  {num[0]}')


# VALIDAÇÃO DOS NÚMEROS:
# num = int(input('Informe um número entre 0 e 9999: '))
# n = num.split()
# if num < 0 or num > 9999:
#     print('Número inválido')
# else :
#     print(f'Unidade: {n}')