pessoas = {'nome' : 'João', 
           'sexo' : 'M', 
           'idade': 27
           }

# print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())

# brasil = list()
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)

# print(brasil[0]['uf'])


estado = dict()
brasil = list()

for c in range(0, 2) :
    estado['uf'] = str(input('Unidade Ferderativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for e in brasil :
    for k, v in e.items() :
        print(f'O campo {k} tem valor {v}')
    # for v in e.values():
    #     print(v, end="-")
    print()