from random import choice

# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

nomes = []

for i in range(1, 5):
    nomes.append(input(f'Digite o nome do {i}° aluno: '))
    if(i > 5):
        break

escolha = choice(nomes)
print(f'O aluno escolhido foi {escolha}')