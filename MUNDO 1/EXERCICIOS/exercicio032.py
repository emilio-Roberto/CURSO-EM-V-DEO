#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = float(input('Digite um ano qualquer: '))
if ano % 4 == 0:
    print('Uau, {:.0f} é um ano bissexto!'.format(ano))
else:
    print('Esse ano foi muito comum.')
#Corrigido
