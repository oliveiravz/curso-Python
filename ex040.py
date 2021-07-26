# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota: '))

while nota1 < 0 or nota1 > 10 :
    print('Nota inválida!! Digite novamente: ')
    nota1 = float(input('Digite a primeira nota: '))

nota2 = float(input('Digite a segunda nota: '))

while nota2 < 0 or nota2 > 10 :
    print('Nota inválida!! Digite novamente: ')
    nota2 = float(input('Digite a primeira nota: '))

media = (nota1 + nota2) / 2

if media < 5 :
    print('Reprovado')
elif media >= 5 and media <= 6.9 :
    print('Recuperação')
else :
    print('Aprovado')