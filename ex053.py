# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

frase = input('Digite uma frase para verfificarmos se ela é um palíndromo: ').strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for c in range(len(junto) -1, -1, -1):
    inverso += junto[c]

if inverso == junto :
    print('Temos um palíndromo')
else: 
    print('A frase digitada não é um palíndromo')