def leiaInt(msg) :
    while True :
        try :
            num = int(input(msg))
        except (ValueError, TypeError) :
            print('\033[31mErro! Digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt :
            print('\033[33mPrograma interrompido pelo usuário\033[m')
            quit()
        else :
            return num

def linha() :
    tamanho = '=' * 50
    return tamanho

def cabecalho(txt) :
    print(linha())
    print(txt.center(50))
    print(linha())

def menu(lista) :
    cabecalho('\033[;1mMENU PRINCIPAL\033[m')
    c = 1 
    for item in lista :
        print(f'\033[1;93m{c}\033[m - \033[1;92m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc