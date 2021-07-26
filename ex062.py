# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('=' * 20, 'PROGRESSÃO ARITMETICA', '=' * 20)

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Informe a razão: '))
mais = 10
c = 0 
total = 0

while mais != 0 :
    total += mais
    while c < total :
        print(termo)
        termo += razao
        c += 1
    mais = int(input('Quer imprimir mais quantos termos? : '))
print(f'Foram mostrados {c} números nessa progressão aritmetica')
print('Fim!')