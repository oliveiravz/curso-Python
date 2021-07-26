# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota = float(input('Informe a 1ª nota do aluno: '))
nota2 = float(input('Informe a 2ª nota do aluno: '))
media = (nota + nota2) / 2
print('A média do aluno é: {:.1f}'.format(media))