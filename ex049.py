# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número: '))

print('='*15)
for i in range(1, 11):
    tab = n * i
    print(f'{n} x {i:2} = {tab:02}')
print('='*15)