# Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

alt = float(input('Informe a altura: '))
lar = float(input('Informe a largura: '))
a = lar * alt
lt = a / 2
print('Voce precisará de {} litros de tinta, para pintar {}m²'.format(lt, a))
