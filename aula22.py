from uteis import numeros

n = int(input('Digite um valor: '))
f = numeros.fatorial(n)
print(f'O fatorial de {n}! é {f}')
print(f'O dobro de {n} é {numeros.dobro(n)}')
print(f'O triplo de {n} é {numeros.triplo(n)}') 