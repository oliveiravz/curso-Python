# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
cont = frase.count('A')
pri = frase.find('A')
ult = frase.rfind('A')

print(f'A letra A aparece {cont} vezes')
print(f'A letra A aparece pela primeira vez na posição {pri + 1}')
print(f'A letra A aparece pela última vez na posição {ult + 1}')
