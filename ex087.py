# Aprimore o desafio anterior, mostrando no final:                                                    
# A) A soma de todos os valores pares digitados.                                                                                                  
# B) A soma dos valores da terceira coluna.                                                                                                               
# C) O maior valor da segunda linha.

matriz = [0] * 3
soma = soma3Coluna = maior = 0

for linha in range(3) :
    matriz[linha] = [0] * 3
    for coluna in range(3) :
        matriz[linha][coluna] = int(input(f'Digite uma valor: '))

        if matriz[linha][coluna] % 2 == 0 :
            soma += matriz[linha][coluna]

        soma3Coluna += matriz[linha][2]

for coluna in range(0, 3) :
    if coluna == 0 :
        maior = matriz[1][coluna]
    elif matriz[1][coluna] :
        maior = matriz[1][coluna]

print('=' * 30)
for linha in range(3) :
    for coluna in range(3) :
        print(f'{matriz[linha][coluna]}', end=' ')
    print()
print(f'\nA soma dos números pares: {soma}')
print(f'A soma da terceira coluna: {soma3Coluna}')
print(f'O maior valor da segunda coluna: {maior}')