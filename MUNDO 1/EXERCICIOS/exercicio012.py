#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Qual o preço do produto: R$'))
cal1 = ((5 * p) / 100)
cal2 = (p - cal1)
print('O preço do produto era R${:.2f}. Mas com 5% de desconto fica R${:.2f}'.format(p, cal2))
#Corrigido