# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print('=-' * 30)
print('Analisando Triângulo')
print('=-' * 30)
ladoA = float(input('Informe o tamanho da primeira reta: '))
ladoB = float(input('Informe o tamanho da segunda reta: '))
ladoC = float(input('Informe o tamanho da terceira reta: '))

cores = {'limpa' : '\033[m', 'azul' : '\033[34m'}
if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB :
    print('O triângulo pode existir')
    if ladoA == ladoB and ladoB == ladoC:
        print('O triângulo é EQUILÁTERO')
    elif ladoA == ladoB or ladoB == ladoC or ladoA == ladoC :
        print('O triângulo é ISÓCELES')
    else :
        print('O triãngulo é ESCALENO')
else:
    print('{}O triângulo não pode existir{}'.format(cores['azul'], cores['limpa']))