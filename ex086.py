# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [0] * 3

for linha in range(3) :
    matriz[linha] = [0] * 3
    for coluna in range(3) :
        matriz[linha][coluna] = int(input(f'Digite uma valor: '))

print('=' * 30)
for linha in range(3) :
    for coluna in range(3) :
        print(f'{matriz[linha][coluna]}', end=' ')
    print()