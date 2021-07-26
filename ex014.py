# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Informe a temperatura em °C: '))
cf = (c * 9/5) + 32
ck = c + 273.15
fc = (cf - 32) * 5/9
print('{} °C = {} °F'.format(c, cf))
print('{} °F = {} °C'.format(cf, c))
print('{} °C = {} °K'.format(c, ck))
