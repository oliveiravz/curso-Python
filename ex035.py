# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('=-' * 30)
print('Analisando Triângulo')
print('=-' * 30)
ladoA = float(input('Informe o tamanho da primeira reta: '))
ladoB = float(input('Informe o tamanho da segunda reta: '))
ladoC = float(input('Informe o tamanho da terceira reta: '))

cores = {'limpa' : '\033[m', 'azul' : '\033[34m'}
if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB :
    print('O triângulo pode existir')
else:
    print('{}O triângulo não pode existir{}'.format(cores['azul'], cores['limpa']))