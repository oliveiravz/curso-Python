# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for c in range(1, 7) :
    n = int(input(f'Digite o {c}º número: '))
    if c % 2 == 0 :
        soma += c
print(f'A soma dos pares dos números digitados é: {soma}')