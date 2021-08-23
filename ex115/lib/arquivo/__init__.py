from interface import *

def arquivoExiste(nome) :
    try :
        a = open(nome, 'rt') # rt = Read Text
        a.close()
    except FileNotFoundError :
        return False
    else :
        return True


def criarArquivo(nome) :
    try :
        a = open(nome, 'wt+') # wt+ = Write Text
        a.close()
    except :
        print('Houve um erro na criação do arquivo')
    else :
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome) :
    try :
        a = open(nome, 'rt')
    except :
        print('Houve um problema ao ler o arquivo')
    else :
        cabecalho('PESSOAS CADASTRADAS')
        cont = 0
        for linha in a :
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{cont + 1} - {dado[0]:<30}{dado[1]:>3} anos')
            cont += 1
        print(f'Total de pessoas cadastradas: {cont}')
    finally :
        a.close()


def cadastrar(arq, nome = 'desconhecido', idade = 0) :
    try :
        a = open(arq, 'at')
    except :
        print('Houve um erro ao abrir o arquivo!')
    else :
        try :
            a.write(f'{nome};{idade}\n')
        except :
            print('Houve um erro ao escrever o arquivo')
        else :
            print(f'Novo registro de {nome} cadastrado')
            a.close()