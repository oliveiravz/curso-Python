# < ----------------------------------- INTERACTIVE HELP ----------------------------------- >

# help(print())
# print(input.__doc__)


# < ------------------------------------- DOCSTRINGS -------------------------------------- >

def contador(i, f, p) :
    """
    -> Faz a contagem e mostra na tela
    :param i: inicio da contagem
    :param f: final da contagem
    :param p: passo da contagem
    :return : sem retorno
    """
    # c = i
    # while c <= f :
    #     print(f'{c}', end='...')
    #     c += p 
    # print('FIM!!')

# contador(2, 10, 2)    
# help(contador)

# < --------------------------------- PARAMETROS OPCIONAIS ----------------------------------- >

# def somar(a=0, b=0, c=0) :
#     """
#     -> Faz a soma de três valores e mostra o valor na tela
#     :param a: primeiro valor
#     :param b: segundo valor
#     :param c: terceiro valor
#     :return: não tem retorno

#     """
#     s = a + b + c 
#     print(f'A soma é : {s}')

# somar(3, 2, 5)


# < --------------------------------- ESCOPO DE VARIÁVEIS ----------------------------------- >
# def teste() :
    x = 8 # ---> A variável x é de escopo local
    # print(f'Na função teste, n vale {n}')
    # print(f'Na função teste, x vale {x}')

# PROGRAMA PRINCIPAL

# n = 2 # ---> A variável n é de escopo global
# print(f'No programa principal, n vale {n}')
# print(f'No programa principal, x vale {x}') ---> A variável x não funciona fora da função teste()

# def funcao() :
#     global n1 
#     print(f'N1 dentro vale {n1}')

# n1 = 2
# funcao()
# print(f'N1 fora vale {n1}')


# < --------------------------------------- RETORNO DE VALORES ------------------------------------>

# def somar(a=0, b=0, c=0) :
#     """
#     -> Faz a soma de três valores e mostra o valor na tela
#     :param a: primeiro valor
#     :param b: segundo valor
#     :param c: terceiro valor
#     :return: não tem retorno

#     """
#     s = a + b + c 
#     return s

# resp = somar(1, 5, 7)

# print(f'O resultado é {resp}')


def fatorial(num = 1) :
    f = 1 
    for c in range(num, 0, -1) :
        f *= c
    return f 

n = int(input('Digite um número: '))
r = fatorial(n)
print(f'O faotiral de {n}! é {r}')