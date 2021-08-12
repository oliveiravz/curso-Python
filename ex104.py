# Crie um programa que tenha a função leiaInt(), 
# que vai funcionar de forma semelhante ‘a função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(numero) :
    v = 0
    ok = False
    while True :
        n = str(input(numero))
        if n.isnumeric() :
            v = int(n)
            ok = True
        else :
            print('Erro digite um número inteiro válido') 
        if ok :
            break
    return v

num = leiaInt('Digite um número: ')
print(f'Você digitou o número {num}')