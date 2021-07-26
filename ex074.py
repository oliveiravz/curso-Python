from random import sample

# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

t = tuple(sample(range(10), 5))

for i in t :
    print(f'Números gerados na Tupla: {t}')
    print(f'Maior número da Tupla: {max(t)}\nMenor número da Tupla: {min(t)}')
    quit()