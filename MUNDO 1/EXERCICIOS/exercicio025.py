#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

n = str(input('Digite seu nome completo: ')).title()
print('Seu nome tem Silva ? {}'.format('Silva' in n))
#Corrigido