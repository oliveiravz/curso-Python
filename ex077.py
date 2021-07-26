# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('ESTUDOS', 'PROGRAMACAO', 'CURSO', 'PYTHON')

for p in palavras :
    print(f'\nNa palavra {p} temos as vogais ', end='')

    for vogais in p :
        if vogais.upper() in 'AEIOU' :
            print(vogais, end=' ')
