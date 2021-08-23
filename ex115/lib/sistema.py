from interface import *
from arquivo import * 
from time import sleep

# cabecalho('SISTEMA ARQUIVO 1.0v')
arq = 'pessoas.txt'

if not arquivoExiste(arq) : 
    criarArquivo(arq)

while True :
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1 :
        lerArquivo(arq)
    elif resposta == 2 :
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade  )
    elif resposta == 3 :
        print('Saindo do sistema!')
        break
    else :
        print('\033[1;91mERRO!! Digite opção válida\033[m')
    sleep(1)