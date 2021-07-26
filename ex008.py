# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite um número, em metros: '))
cm = m * 100
mm = m * 1000
dc = m * 0.1
hc = m * 0.01
km = m * 0.001
print('{} metros são {} centímetros'.format(m, cm))
print('{} metros são {} milimetros'.format(m, mm))
print('{} metros são {} decametros'.format(m, dc))
print('{} metros são {} hectometros'.format(m, hc))
print('{} metros são {} quilometros'.format(m, km))