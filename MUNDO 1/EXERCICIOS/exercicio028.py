#Escreva um programa que faça o computador "pensar em um número inteiro entre 0 e 5 e 
#peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

'''print('---ADIVINHA MILIONAIRE---')
print('Carregando...')
n = random.randint(0,5)
print('Estou pensando em um número...')
user = int(input('Digite o número que ele pensou: '))
if user == n:
    print('Poxa!! Como você sabia? GRRR')
    print('PARABÊNS')
else:
    print('HAHAHA Não foi dessa vez Perdedor!!')
print('O Número em que eu pensei é: {}'.format(n))'''
#Corrigido

from time import sleep

print('---ADIVINHA MILIONAIRE---')
print('Carregando...')
sleep(2)
n = random.randint(0,5)
print('Estou pensando em um número...')
sleep(5)
user = int(input('Digite o número que ele pensou: '))
if user == n:
    print('Poxa!! Como você sabia? GRRR')
    print('PARABÊNS')
else:
    print('HAHAHA Não foi dessa vez Perdedor!!')
print('O Número em que eu pensei é: {}'.format(n))
