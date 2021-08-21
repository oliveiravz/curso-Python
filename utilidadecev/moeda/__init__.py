def metade(n = 0, formato=False) :
    n /= 2

    return n if not formato else moeda(n)

def dobro(n = 0, formato=False) :
    n *= 2

    return n if not formato else moeda(n)

def aumentando(n = 0, p = 0, formato=False) :
    r = n + ((n * p) / 100)

    return r if not formato else moeda(r)

def reduzindo(n = 0, p = 0, formato=False) :
    r = n - ((n * p) / 100)

    return r if not formato else moeda(r)

def moeda(n = 0, m = 'R$') :
    return f'{m}{n:.2f}'.replace('.', ',')

def resumo(preco = 0, taxaa = 10, taxab = 5 ) :
    print('=' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('=' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentando(preco, taxaa, True)}')
    print(f'{taxab}% de diminuição: \t{reduzindo(preco, taxab, True)}')
    print('=' * 30)