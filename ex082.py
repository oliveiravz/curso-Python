# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

numeros = []
pares = []
impares = []
cont = 0
op = ''

while True :
    num = int(input('Digite um número: '))
    numeros.append(num)
    cont += 1

    if num % 2 == 0 :
        pares.append(num)
    else :
        impares.append(num)
    
    op = str(input('Quer continuar?[S/N]: ')).lower()

    if op == 'n' :
        print('=' * 20) 
        print(f'Números digitados: {numeros}')
        print(f'Números pares: {pares}')
        print(f'Números impares: {impares}')
    