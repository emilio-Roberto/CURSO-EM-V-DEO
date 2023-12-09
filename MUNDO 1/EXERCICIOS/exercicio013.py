#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
SA = float(input('Qual o salário do trabalhador: R$'))
au = SA + (15 * SA / 100)
print('O sslário antigo era de R${:.2f}. Mas com um aumento de 15%, foi para R${:.2f}.'.format(SA, au))
#Corrigido