# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

print('=' * 20, 'TUPLAS', '=' * 20)

extenso = ( 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito',
            'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
            'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')


while True :
    valor = int(input('Digite um valor entre 0 e 20: '))
    while valor not in range(0, 21) :
        valor = int(input('Número inválido! Tente novamente: '))

    for cont in range(0, len(extenso)) :
        if valor == cont :
            print(f'Você digitou {extenso[cont]}')
