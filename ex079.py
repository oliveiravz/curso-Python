# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.



numeros = []
opcao = ''

while True :
    num = int(input('Digite um número: '))
    if num in numeros :
        print('Valores duplicados não serão adicionados')
    else :
        numeros.append(num)
        print('Valor adicionado com sucesso!')

    opcao = str(input('Deseja continuar?[S/N]: ')).upper()
    while opcao not in 'SN' :
        opcao = str(input('Opcao inválida! Tente novamente: ')).upper()

    if opcao == 'N' :
        print('=' * 20)
        print(f'Você digitou {sorted(numeros)}')
        break