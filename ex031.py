# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('Digite a distância da viagem (km): '))

if dist <= 200:
    preco = dist * 0.50
    print(f'A sua viagem custará: R${preco:.2f}')
else:
    preco = dist * 0.45
    print(f'A sua viagem custará: R${preco:.2f}')