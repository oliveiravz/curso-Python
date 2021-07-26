# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.

op = 0
soma = 0
mult = 1
maior = 0
n = []

print('=' * 20, 'MENU PYTHON', '=' * 20)

while True :
    for i in range(2) :
        num = int(input(f'Digite o {i+1}º número: '))
        n.append(num)

    # while op != 5 :
    print('\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa ')
    print()
    op = int(input('Escolha a opção: '))
        
    if op == 1 :
        for i in range(2) :
            soma += n[i]
        print(f'A soma dos números: {soma}')

    if op == 2 :
        # mult = 1
        for i in range(2) :
            mult *= n[i]
        print(f'A multiplicação dos números: {mult}')

    if op == 3 :
        for i in range(2) :
            if i == 0 :
                maior = n[i]
            if n[i] > maior :
                maior = n[i]
        print(f'O maior número: {maior}')

    if op == 4 :
        print('Digite novos números!')
        for i in range(2) :
            num = int(input(f'Digite o {i+1}º número: '))
            n.append(num)


    if op == 5 :
        print('FIM!')
        quit()
        




