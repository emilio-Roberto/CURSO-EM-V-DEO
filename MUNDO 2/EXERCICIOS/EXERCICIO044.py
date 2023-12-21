#Elabore um programa que calcule o valor a ser pago por um produto, 
#considerando o seu preço normal e condição de pagamento: 
#- À vista dinheiro/cheque: 10% de desconto 
#- À vista no cartão: 5% de desconto 
#- Em até 2x no cartão: Preço normal 
#- 3x ou mais no cartão: 20% de juros.

#Entrada
print('Para calcular o valor a ser pago:\n-Digite o preço.\n-Digite a forma de pagamento.')
p = float(input('Digite o valor do produto: R$'))
fpa = int(input('Digite a forma de pagamento:\n1- À vista Dinheiro/Cheque.\n2- À vista no cartão.\n3- Em até 2x no cartão.\n4- 3x ou mais no cartão.\nDigite o número da opção Escolhida: '))
#lógica
op1 = ((10 * p) / 100) 
op2 = ((5 * p) / 100)
op3 = (p)
op4 = ((20 * p) / 100)
#Processamento/Apresentação
if fpa == 1:
    nf = (p - op1) 
    print(f'Valor do produto: R${p:.2f}.\nTotal a pagar: R${nf:.2f}.\nDesconto de 10%.')
elif fpa == 2:
    nf = (p - op2)
    print(f'Valor do produto: R${p:.2f}.\nTotal a pagar: R${nf:.2f}.\nDesconto de 5%.')
elif fpa == 3:
    nf = (op3)
    print(f'Valor do produto: R${p:.2f}.\nTotal a pagar: R${nf:.2f}.\nSem Desconto.')
elif fpa == 4:
    nf = (p - op4)
    print(f'Valor do produto: R${p:.2f}.\nTotal a pagar: R${nf:.2f}.\nJuros de 20%.')
else:
    print('Opção incorreta.')

#Apresentando resultado diferente do descrito nos testes.
    
#Resolução:

'''
print('{!=^40}'.format('LOJAS BERTO'))
p = float(input('Preço das compras R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À Vista dinheiro/PIX
[ 2 ] À Vista Cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x ou Mais no Cartão''')
op = int(input('Qual é a opção ? '))
if op == 1:
    total = p - (p * 10 / 100)
elif op == 2:
    total = p - (p * 5 / 100)
elif op == 3:
     total = p
     par = total / 2
     print('Sua compra será parcelada em 2x de R${:.2f}.'.format(par))
elif op == 4:
    total = p + (p * 20 / 100)
    topar = int(input('Quantas parcelas ? '))
    parcela = total / topar
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(topar, parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(p, total))
'''

#Finalizado
