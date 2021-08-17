from modulos import moeda


p = float(input('Informe um valor: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10% de {moeda.moeda(p)} é {moeda.aumentando(p, 10, True)}')
print(f'Reduzindo 20% de {moeda.moeda(p)} é {moeda.reduzindo(p, 20, True)}')