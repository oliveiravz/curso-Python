# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

preco = float(input('Informe o valor do produto: '))
pag = int(input('Forma de pagamento: \n1 - À vista\n2 - À vista no cartão\n3 - 2x no cartão\n4 - 3x ou mais no cartão\nInforme a forma de pagamento: '))


if pag == 1 :  
    vFinal = preco - ((preco * 10) / 100)
elif pag == 2 :
    vFinal = preco - ((preco * 5) / 100)
elif pag == 3 :
    vFinal = preco / 2

elif pag == 4 :
    vFinal = preco + ((preco * 20) / 100)
    totalParc = int(input('Informe o número de parcelas: '))
    parcelas = vFinal / totalParc
    print(f'Valor: R${preco:.2f}\nParcelas: {totalParc} de R${parcelas:.2f}')
else :
    print('Opção inválida')