# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('Digite qualquer coisa: ')
print('O tipo primitivo desse valor é: ', type(algo))
print('Só tem espaços: {}'.format(algo.isspace()))
print('É numérico: {}'.format(algo.isnumeric()))
print('É alfabetico: {}'.format(algo.isalpha()))
print('É alfanumérico: {}'.format(algo.isalnum()))
print('Está em maiúsculas: {}'.format(algo.isupper()))
print('Está em minúsculas: {}'.format(algo.islower()))
print('Está capitalizada: {}'.format(algo.istitle()))