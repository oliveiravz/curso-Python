# Faça um programa que tenha uma função chamada escreva(), 
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 

def escreva(texto) :
    t = len(texto) + 4
    print('~' * t)
    print(f'  {texto}')
    print('~' * t)

escreva('Olá, mundo!')