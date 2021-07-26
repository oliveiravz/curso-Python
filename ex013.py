# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário R$: '))
a = salario + (salario * 0.15)
print('O novo salário é de: R${:.2f}'.format(a))