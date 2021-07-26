# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Informe um valor: '))
d = n * 2
t = n * 3
rq = n ** (1/2)
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}!'.format(n, d, t, rq))
