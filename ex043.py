# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, 
# de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5 :
    print(f'IMC: {imc:.2f}\nABAIXO DO PESO')
elif imc >= 18.5 and imc <= 25 :
    print(f'IMC: {imc:.2f}\nPESO IDEAL')
elif imc > 25 and imc <= 30 :
    print(f'IMC: {imc:.2f}\nSOBREPESO')
elif imc > 30 and imc <= 40 :
    print(f'IMC: {imc:.2f}\nOBESIDADE')
else :
    print(f'IMC: {imc:.2f}\nOBESIDADE MÓRBIDA')