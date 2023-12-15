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
    