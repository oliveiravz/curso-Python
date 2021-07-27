# Faça um programa que leia nome e média de um aluno, 
# guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
dado  = list()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))

print(f"O nome é {aluno['nome']}")
print(f"A media é {aluno['media']}")

if aluno['media'] >= 7 :
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7 :
    aluno['situacao'] = 'Recuperação'
else :
    aluno['situacao'] = 'Reprovado'

print('=' * 30)

for keys, values in aluno.items():
    print(f'{keys} é igual a {values}')