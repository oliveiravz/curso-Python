# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))

maior = num1

if num1 == num2 :
    print('Não existe valor maior, os dois são iguais')
elif num2 > num1 :
    maior = num2
    print(f'{maior} é maior!')
else :
    print(f'{maior} é maior!')