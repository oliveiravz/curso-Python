# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.


n = int(input('Digite um número: '))
# aux = (n/2) * 2

if n % 2 == 0:
    print(f'{n} é par')
else: 
    print(f'{n} é impar')


# if aux == n:
#     print(f'{n} é par')
# else:
#     print(f'{n} é impar')