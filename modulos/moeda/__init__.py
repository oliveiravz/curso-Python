def metade(n = 0, formato=False) :
    n /= 2

    return n if not formato else moeda(n)

def dobro(n = 0, formato=False) :
    n *= 2

    return n if not formato else moeda(n)

def aumentando(n = 0, p = 0, formato=False) :
    r = ((n * p) / 100) + n

    return r if not formato else moeda(n)

def reduzindo(n = 0, p = 0, formato=False) :
    r = n - ((n * p) / 100)

    return r if not formato else moeda(n)

def moeda(n = 0, m = 'R$') :
    return f'{m}{n:.2f}'.replace('.', ',')