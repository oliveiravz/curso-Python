# teste = list()
# teste.append('Joao')
# teste.append(27)
# galera = list()
# # [:] É uma cópia da lista ##
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)]


# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# print(galera[0][1])
# print(galera[2][0])

# for p in galera :
#     print(p[1])

galera = dado = list()

for c in range(0, 3) :
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    # Limpa o append, nesse caso limpa as duas listas
    dado.clear()
    print(galera)

totalMaior = totalMenor = 0
for p in galera :
    if p[1] >= 21 :
        print(f'{p[0]} é maior de idade!')
        totalMaior += 1
    else :
        print(f'{p[0]} é menor de idade!')
        totalMenor += 1
    
print(f'Temos {totalMaior} maiores e {totalMenor} menores de idade!')