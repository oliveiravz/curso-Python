# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 
# 2 para octal e 
# 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))
base = int(input('Informe a base para conversão-\n1 para binário\n2 para octal\n3 para hexadecimal\nDigite: '))

if base == 1 :
    print(f'{num} para decimal é igual a {bin(num)[2:]}')
elif base == 2 :
    print(f'{num} para octal é igual a {oct(num)[2:]}')
elif base == 3 :
    print(f'{num} para exadecial é igual a {hex(num)[2:]}')
else :
    print('Opção inválida')