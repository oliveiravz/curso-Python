import math
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

''' Fórmula matemática seno = cateto oposto / hipotenusa
    Fórmula matemática coseno = cateto adjacente / hipotenusa
    Fórmula matemática tangente = cateto oposto / adjacente'''

num = float(input('Informe um ângulo qualquer: '))
#print('Seno = {:.2f}\nCoseno = {:.2f}\nTangente = {:.2f}'.format(math.sin(num), math.cos(num), math.tan(num)))
''' PARA CONSEGUIR CALCULAR SEN, COSENO E TANGENTE PRIMEIRO TEM QUE CONVERTER OS VALORES PARA RADIANOS '''
senn = math.sin(math.radians(num))
coss = math.cos(math.radians(num))
tann = math.tan(math.radians(num))
print('O seno do ângulo {}° é: {:.2f}'.format(num, senn)) 
print('O coseno do ângulo {}° é: {:.2f}'.format(num, coss)) 
print('A tangente do ângulo {}° é: {:.2f}'.format(num, tann)) 