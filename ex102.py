# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
# o primeiro que indique o número a calcular e outro chamado show, 
# que será um valor lógico (opcional) indicando se será mostrado ou não 
# na tela o processo de cálculo do fatorial.

def fatorial(num = 1, show=False) :
    f = 1 
    for i in range(num, 0, -1) :
        if show :
            print(f'{i}', end='')
            if i > 1 :
                print(f' x ', end='')
            else :
                print(' = ', end='')
        f *= i
    return f

print(fatorial(5, show=True))
# print(fatorial(5))