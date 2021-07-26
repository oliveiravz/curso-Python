from math import hypot
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.

# Fórmula para encontrar a hipotenusa segundo a matemática:
# a² = b² + c² 

co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
hi = hypot(co, ca)

#hi = (co ** 2 + ca ** 2) ** 1/2 - sem importação
print('Cateto Oposto = {}\nCateto Adjacente = {}\nHipotenusa = {:.2f}'.format(co, ca, hi))
