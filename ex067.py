# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

print('=' * 10, 'Tabuada v3.0', '=' * 10)
rasp = 0
while True :
    print()
    tab = int(input('Quer ver a tabuada de qual valor: '))

    if tab < 0 :
        print('Programa finalizado!')
        break

    for i in range(1, 10) :
        resp = tab * i
        print(f'{tab} x {i} = {resp}')

