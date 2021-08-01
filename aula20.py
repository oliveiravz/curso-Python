def lin():
    print('=' * 30)

# Programa principal 
lin()
print('     CURSO EM VÍDEO      ')
lin()

def mensagem(msg):
    print('=' * 30)
    print(msg)
    print('=' * 30)

# Programa principal
mensagem('  Aprenda Python  ')


def soma(a, b) :
    s = a + b
    print(s)

# Programa principal
soma(4, 5)
soma(a=4, b=5)
soma(b=4, a=5)


def contador(* num) :
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(2, 1, 7)

def dobra(lst) :
    pos = 0
    while pos < len(lst) :
        lst[pos] *= 2 
        pos += 1

valores = [6, 8, 4, 5, 1] 
dobra(valores)
print(valores)