#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex: Digite o número 6.127. O número 6.127 tem a parte Inteira 6.

'''num = float(input('Digite um número com virgula ex:6,127 '))
print('Seu número digitado tem a parte inteira: ({:.0f})'.format(num))'''

#ou

'''num = float(input('Digite um número com virgula ex:6,127 '))
print('Seu número digitado tem a parte inteira: ({:.0f})'.format(int(num)))'''

#ou

from math import trunc

n = float(input('Digite um número: '))
print('O número digitado {} tem a parte inteira {}'.format(n, trunc(n)))
#Corrigido
