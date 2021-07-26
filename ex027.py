# Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o seu nome completo: ')).strip()
n = nome.split()

pri = n[0]
ult = n[len(n)-1]

print(30*'=')
print('Muito prazer em te conhecer!')
print(f'O seu primeiro nome é {pri}')
print(f'O seu último nome é {ult}')
