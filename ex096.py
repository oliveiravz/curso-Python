#  Faça um programa que tenha uma função chamada área(), 
#  que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(b, h) :
    a = b * h
    print(f'A área do seu terreno {b:.1f}x{h:.1f} é de {a:.1f}m².')

print('=' * 30)
print('CONTROLE DE TERRENOS')
print('=' * 30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
# print(area)