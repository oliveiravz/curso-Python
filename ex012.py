# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

v = float(input('Digite o valor da compra: '))
d = v - (v * 0.05) 
print('Valor à prazo: R${}'.format(v))
print('Valor à vista: R${}'.format(d))
