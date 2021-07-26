# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primTermo = int(input('Informe o primeiro termo da progressão aritmética: '))
razao = int(input('Agora informe a razão: '))
cont = 1
 
while cont <= 10 :
    print(f'{primTermo}')
    primTermo += razao
    cont += 1