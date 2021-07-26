# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Informe o valor da casa: '))
salario = float(input('Informe o salário do comprador: '))
anos = int(input('Informe em quantos anos pretende financiar: '))

prestacao = valor / (anos * 12)

if valor < 0 or salario < 0 or anos < 0 :
    print('Informe os dados corretamente!')
elif prestacao > (salario * 30) / 100 :
    print('A valor da prestação excede 30% do seu salário\nEmpréstimo Negado!')
else :
    print(f'Empréstimo concedido!!\nTotal a pagar: R${valor:.2f}\nPrestação: {anos * 12} parcelas de R${prestacao:.2f}')
    