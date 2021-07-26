# () = tupla
# [] = lista
# {} = Dicionário

# Tuplas são imutáveis:
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

# Em ordem alfabética, nesse caso
print(sorted(lanche))
print()
for comida in lanche :
    print(f'Eu vou comer {comida}')
print()
# Ideal para mostrar a posição da Tupla
for cont in range(0, len(lanche)) :
    print(f'eu vou comer {lanche[cont]} na posição {cont}')
print()
# Outra maneira de mostrar posição
for pos, comida in enumerate(lanche) :
     print(f'eu vou comer {comida}, na posição {pos}')

# print(len(lanche))

print('Fim!')


# ========== COM NÚMEROS =========== #

# a = (1, 2, 3 , 4)
# b = (10, 20, 30, 40)
# c = a + b
# print(c)
# print(len(c))

# # Conta quantas vezes aparece o elemento setado
# print(c.count(2))

# # Mostra qual a posição do elemento
# #  0  1  2  3  4   5   6   7
# # [1, 2, 3, 4, 10, 20, 30, 40]
# print(c.index(2, 5))
