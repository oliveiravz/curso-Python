# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome: '))

# split() --> separa as palavras de uma string
pri = nome.split()

# replace() --> nesse caso, retira os espaços da string
nom = nome.replace(' ', '')


print(f'Letras maíusculas: {nome.upper()}')
print(f'Letras minúsculas: {nome.lower()}')
# --> len() conta as posições da string
print(f'O seu nome tem {len(nom)} letras totais') 
# --> len(pri[0]) printa somente a posição setada
print(f'O seu 1° nome tem {len(pri[0])} letras')
