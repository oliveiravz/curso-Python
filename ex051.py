# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primTermo = int(input('Informe o primeiro termo da progressão aritmética: '))
razao = int(input('Agora informe a razão: '))

for c in range(primTermo, primTermo + 10) :
    print(primTermo)
    primTermo += razao
    # print(c)
