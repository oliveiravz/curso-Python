# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Informe a velocidade do veículo: '))
veLimite = 80
multa = 7

if vel >= veLimite :
    multa = (vel - veLimite) * multa
    print(f'Sua velocidade foi de {vel:.2f}Km/h e você foi multado\nSua multa é de: R${multa:.2f}')
else:
    print(f'Continue respeitando as leis de trânsito!')