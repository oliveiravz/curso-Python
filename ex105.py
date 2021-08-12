# Faça um programa que tenha uma função notas() que pode receber várias notas de 
# alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas                                                                                                                                                 
# – A maior nota                                                                                                                                                                
# – A menor nota                                                                                                                                                              
# – A média da turma                                                                                                                                                      
# – A situação (opcional)


def notas(* nt, situacao = False) :
    aluno = dict()
    aluno['maior'] = max(nt)
    aluno['menor'] = min(nt)
    aluno['media'] = sum(nt) / len(nt)
    
    if situacao :
        if aluno['media'] >= 7 :
            aluno['situacao'] = 'BOA'
        elif aluno['media']  >= 5 :
            aluno['situacao'] = 'RAZOÁVEL'
        else :
            aluno['situacao'] = 'RUIM'
    return aluno

resp = notas(3, 5, 6, 7, situacao=True)   
print(resp)