# Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

media = maior = menor = cont = soma = 0

while True :
    nm = int(input('Digite um número: '))
    op = str(input('Quer continuar? [s/n]: ')).lower()

    while op != 'n' and op != 's' :
        op = str(input('Opção inválida! Tente novamente: '))

    cont += 1
    soma += nm
    media = soma / cont

    if cont == 1 :
        maior = nm
        menor = nm
    if nm > maior :
        maior = nm
    if nm < menor :
        menor = nm

    if op == 'n' :
        print(f'A média dos números digitados: {media}')
        print(f'Maior: {maior}\nMenor: {menor}')
        quit()
