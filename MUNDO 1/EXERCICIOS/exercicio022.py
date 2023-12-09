#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas 
#- O nome com todas minúsculas 
#- Quantas letras ao todo(sem considerar espaços) 
#- Quantas letras tem o primeiro nome.

n = str(input('Digite seu nome completo: '))
n1 = n.upper()
n2 = n.lower()
n3cont = len(n)
n3 = n3cont - n.count(' ') 
n4 = n.split()

print('''Seu nome todo em maiúsculo: {}
Seu nome todo em minúsculo: {}
Quantas letras tem ao todo: {}
Quantas letras tem o primeiro nome: {}'''.format(n1, n2, n3, len(n4[0])))
#Corrigido

#ou

'''n = str(input('digite seu nome completo: '))
print('Analisando seu nome...')
print('Seu nome em Maúsculo é {}'.format(n.upper()))
print('Seu nome em Minúsculo é {}'.format(n.lower()))
print('Seu nome tem ao todo {} letras!'.format(len(n) - n.count(' ')))
sep = n.split()
print('Seu primeiro nome é {} e ele tem {} letras!'.format(sep[0], len(sep[0])))'''
