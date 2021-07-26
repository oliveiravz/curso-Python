# Crie um programa que vai ler vários números e colocar em uma lista.                  
# Depois disso, mostre:                                                                                                                                                
# A) Quantos números foram digitados.                                                                                                                    
# B) A lista de valores, ordenada de forma decrescente.                                                                                          
# C) Se o valor 5 foi digitado e está ou não na lista.

numeros = []
cont = cont5 = 0
op = 'N'

while True :
    num = int(input('Digite um número: '))
    # if cont == 0 or num < numeros[-1] :
    numeros.append(num)
    cont += 1

    op = str(input('Quer continuar?[S/N]: ')).upper()
    while op not in 'SN' :
        op = str(input('Quer continuar?[S/N]: ')).upper()

    if op == 'N' :
        if 5 not in numeros :
            print('O número 5 não foi digitado')
        else :
            print(f'O número 5 foi digitado')
        
        print(f'Foram digitados {cont} números')
        print(f'{sorted(numeros, reverse=True)}')
        break