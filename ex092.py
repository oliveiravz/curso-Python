import datetime

# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

trabalhador = dict()
contribuicao = 35

trabalhador['Nome'] = str(input('Nome: '))
trabalhador['Nascimento'] = int(input('Ano de nascimento: '))
trabalhador['CDT'] = int(input('Carteira de trabalho: '))

if trabalhador['CDT'] != 0 :
    trabalhador['contratacao'] = int(input('Ano de contratação: '))
    trabalhador['Salario'] = float(input('Salario: R$'))

data = datetime.date.today().year
trabalhador['Idade'] = data - trabalhador['Nascimento']
tempo = trabalhador['contratacao'] - data
trabalhador['Aposentadoria'] = trabalhador['idade'] + (trabalhador['contratacao'] + 35) - data

print('=' * 30)
for key, values in trabalhador.items() :
    print(f'{key}: {values}')