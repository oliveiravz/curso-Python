# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.

base = 1250
aum10 = 0.10
aum15 = 0.15
salario = float(input('Informe o salário: '))

if salario <= base :
    salario += salario * aum15
    print(f'Novo salário: R${salario:.2f}')
elif salario >= base : 
    salario += salario * aum10
    print(f'Novo salario: R${salario:.2f}')