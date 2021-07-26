# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.


produtos = ('Notebook', 3600, 'Mouse', 159.99, 'Monitor 144Ghz', 1699, 'Placa de vídeo', 3700)

precos = 0
nomes = ''

print('=' * 40)
print(f'{"TABELA DE PREÇOS":^30}')
print('=' * 40)

for i in range(0, len(produtos)) :
    if i % 2 == 0 :
        print(f'{produtos[i]:.<30}', end='')
    else :
        print(f'R${produtos[i]:>10.2f}')