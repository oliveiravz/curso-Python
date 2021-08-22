try :
    a = int(input('Numerador: '))
    b = int(input('Denomidador: '))
    r = a / b
except (ValueError, TypeError) : #Erro de valor e Erro de tipo de dados
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError : #Erro ao dividir por zero
    print('Não é possível dividir por zero')
except KeyboardInterrupt : #Interrupção pelo teclado ctrl + c
    print('O usuário decidiu encerrar o programa')
except Exception as erro : # Erro personalizado
    print(f'O erro encontrado foi {erro.__cause__}')
else :
    print(f'O resultado entre {a} / {b} = {r:.1f}')
finally :
    print('Muito obrigado! Volte sempre!')