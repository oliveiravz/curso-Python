# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

op = 's'
while op == 's' :
    sexo = input('Informe o seu sexo [F - M]: ' ).lower()
    while sexo != 'f' and sexo != 'm' :
        sexo = input('Opção inválida! Tente novamente [F - M]: ' ).lower()
    op = input('Deseja informar novamente?: ')
    if sexo == 'f' :
        print('Feminino')
    if sexo == 'm' :
        print('Masculino')
    break