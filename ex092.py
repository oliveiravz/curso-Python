# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

trabalhador = dict()

trabalhador['nome'] = str(input('Nome: '))
trabalhador['nascimento'] = int(input('Ano de nascimento: '))
trabalhador['CDT'] = int(input('Carteira de trabalho: '))
trabalhador['salario'] = float(input('Salario R$ '))

if trabalhador['CDT'] == 0 :
    quit()

print(trabalhador)