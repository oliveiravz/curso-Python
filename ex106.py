
#  Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.

def ajuda(c) :
    help(c)


cor = [
    '\033[31m',                 # vermelho
    '\033[32m',                 # verde 
    '\033[33m',                 # amarelo
]

print('=' * 30)
print(f"{'SISTEMA DE AJUDA PYTHON':^30}")
print('=' * 30)

while True :
    a = str(input('Função ou biblioteca >> '))
    if a.upper() == 'FIM' :
        break
    else :
        ajuda(a)

print(cor[2], '=' * 30)
print(cor[2], 'PROGRAMA FINALIZADO')
print(cor[2], '=' * 30)