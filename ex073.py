# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

print('='*20,'TABELA BRASILEIRÃO','='*20)

ache = ''
tabela = ('Palmeiras',
          'Atlético-MG',
          'Fortaleza',
          'Bragantino',
          'Fortaleza',
          'Atlhetico-PR',
          'Flamengo',
          'Ceará',
          'Bahia',
          'Fluminense',
          'Santos',
          'Atlético-GO',
          'Corinthians',
          'Internacional',
          'Juventude',
          'São Paulo',
          'Sport Recife',
          'América-MG',
          'Cuiabá',
          'Grêmio',
          'Chapecoense')

print('Os 5 primeiros colocados')
for i in range(1, 6) :
    print(f'{i}º {tabela[i]}')
print()
print('Os 5 últimos colocados')
for i in range(15, 21) : 
    print(f'{i}º {tabela[i]}')
print()
print('ORDEM ALFABÉTICA')
print(f'{sorted(tabela)}')

if 'Chapecoense' in tabela :
    print(f"A Chapecoense está na posição: {tabela.index('Chapecoense') + 1}")