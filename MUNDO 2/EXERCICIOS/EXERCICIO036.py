#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#O salário do comprador e em quantos anos ele vai pagar. 
#Calcule o valor da prestação mensal, sabendo que ele não pode execeder 30% do salário ou então o empréstimo será negado.

print('=====Banco Bradesco Financiamentos=====')
sa = int(input('Digite sua renda bruta por mês: R$'))
valin = int(input('Digite o valor do imovel a ser financiado: R$'))
par = int(input('Em quantas parcelas vai dividir (12 - 24 - 36 - 48 - 60 - 72 - 84 - 96): '))
cal1 = (valin / par )
cal2 = ((sa * 30) / 100)
if cal1 <= cal2:
    print('\033[1:37:42mParabéns!!! Seu financiamento foi aprovado.')
    print('Seu financiamento com valor total de R${:.2f}, Foi aprovado com {} parcelas de R${:.2f}'.format(valin, par, cal1))
else:
    print('\033[1:37:41mDesculpe!! Seu financiamente nã foi aprovado.\nEle execede 30% de sua renda mensal!!')

#Corrigido
