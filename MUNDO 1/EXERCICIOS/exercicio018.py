#Faça um programa que leia um Ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
an = float(input('Digite o ângulo desejado: '))
sen = math.sin(math.radians(an))
print('O ângulo de {} tem o SENO {:.2f}.'.format(an, sen))
cos = math.cos(math.radians(an))
print('O ângulo de {} tem o COSSENO {:.2f}.'.format(an, cos))
tan = math.tan(math.radians(an))
print('O ângulo de {} tem a TANGENTE {:.2f}'.format(an, tan))
#Corrigido
