# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

num = str(input('Digite uma expressão: ')).strip().lower()
exp = []
for i in num :
    if i == '(' :
        exp.append(num)
    elif i == ')' :
        if len(num) > 0:
            exp.pop()
        else :
            exp.append(')')
            break

if len(exp) == 0 :
    print('A expressão está válida')
else :
    print('A expressão está inválida')

