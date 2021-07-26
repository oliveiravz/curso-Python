# Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o 
# programa vai informar quantas cédulas de cada valor serão entregues. 
# OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.



print('=' * 20)
print('CAIXA ELETRÔNICO')
print('=' * 20)

cedula = 50
total = cont = 0

valor = int(input('Valor a ser sacado [somente multiplos de 5]: R$'))
while True :
    if valor >= cedula :
        valor -= cedula
        total += 1
    else :
        if total > 0 :
            print(f'Total de {total} de R${cedula:.2f}')
        if cedula == 50 :
            cedula = 20
        elif cedula == 20 :
            cedula = 10 
        elif cedula == 10 :
            cedula = 1
        total = 0
        if valor == 0 :
            break

    
    
        


