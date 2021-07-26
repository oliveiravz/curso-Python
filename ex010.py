# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

reais = float(input('Digite a quantia em reais: '))
dolar = reais / 5.38
print('Com R${:.2f} você poderá comprar US${:.2f}'.format(reais, dolar))