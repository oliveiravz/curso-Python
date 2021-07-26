# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

# strip() -> Retira os espaços da string
nome = input('Digite seu nome completo: ').strip()

# upper() -> Todas as letras maiúsculas
silva = nome.upper()

if 'SILVA' in silva :
    print('Seu nome tem silva')
else: 
    print('Seu nome não tem silva')