# Crie um programa onde o usuário possa digitar sete valores numéricos e 
# cadastre-os em umal ista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.

numeros = list()
pares   = list()
impares = list()

for i in range(1, 8) :
    numeros.append(int(input(f'Digite o {i}° valor: ')))

for n in numeros :
    if n % 2 == 0 :
        pares.append(n)
    else :
        impares.append(n)

print('=' * 40)
print(f'Números digitados: {numeros}')
print(f'O números pares são: {sorted(pares)}')
print(f'O números ímpares são: {sorted(impares)}')