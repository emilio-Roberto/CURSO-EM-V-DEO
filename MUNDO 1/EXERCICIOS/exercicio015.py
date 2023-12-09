# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias 
#pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = int(input('Quantos dias ficou com o carro ? '))
dia = (d * 60)
km = float(input('Quantos km rodados ? '))
dis = (km * 0.15)
print('Durante o periodo de {} dias, você terá que pagar R${:.2f}. Visto que (R$60/dia)!'.format(d, dia)) 
print('Com {} Km rodados, o total a pagar é R${:.2f}. Visto que (R$0,15/km)!'.format(km, dis))
print('O total a ser pago é R${:.2f}.'.format(dia + dis))
#Corrigido