from random import shuffle

# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

nomes = []

for i in range(1, 5):
    nomes.append(input('Informe o nome do {}° aluno: '.format(i)))
    if(i > 5):
        break

shuffle(nomes)
print('A ordem será: {}'.format(nomes))
