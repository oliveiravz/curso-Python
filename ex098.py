from time import sleep

def contador(ini, fim, passo) :
    if passo < 0 :
        passo *= -1
    if passo == 0 :
        print('Não existe passo 0')
        passo = 1

    print(f'Contagem de {ini} até {fim} com intervalo de {passo} em {passo}')

    if ini < fim :
        cont = ini
        while cont <= fim : 
            print(f'{cont}', end=' ', flush=True)
            sleep(0.3)
            cont += passo
        print('-> FIM!!')
    else :
        cont = ini 
        while cont >= fim :
            print(f'{cont}', end=' ', flush=True)
            sleep(0.3)
            cont -= passo
        print('-> FIM!!')

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez!!!')
i = int(input('Digite o início: '))
f = int(input('Digite o final: '))
p = int(input('Digite o passo: '))

contador(i, f, p)