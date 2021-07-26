# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('=' * 20)
print('COMPRAS')
print('=' * 20)

soma = cont = barato = contP = 0
baratoN = op = ''

while True :
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: '))
    cont += 1

    op = str(input('Quer continuar?[S/N]: ')).upper()
    while op not in 'SN' :
        op = str(input('Quer continuar?[S/N]: ')).upper()

    if cont == 1 :
        barato = preco
        baratoN = nome
    if preco < barato :
        barato = preco
        baratoN = nome
    
    if preco > 1000 :
        contP += 1

    soma += preco

    if op == 'N' :
        break 

print(f'Total gasto: R${soma:.2f}')
print(f'Total de produtos que custam mais de R$1000: {contP}')
print(f'Nome do produto mais barato: {baratoN}')
