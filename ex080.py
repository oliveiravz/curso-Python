# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()). 
# No final, mostre a lista ordenada na tela.

numeros = []

for cont in range(5) :
    num = int(input('Digite um número: ')) 
    if cont == 0 or num > numeros[-1]:
        numeros.append(num)
        print(f'Número adicionado na última posição')
    else :
        posicao = 0
        while posicao < len(numeros) :
            if num <= numeros[posicao] :
                numeros.insert(posicao, num)
                print(f'Número adicionado na posição {numeros.index(num)}')
                break
            posicao += 1
print(numeros)