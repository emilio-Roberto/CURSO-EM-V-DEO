#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados 
#EX: Digite um número: 1834 
#-Unidade:4 
#-Dezena:3 
#-Centena:8 
#-Milhar:1
#com string e matemáticamente

'''n = int(input('Digite um número de 0 a 9999: '))
num = str(n)
print('Analisando....')
print('Unidade; {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))'''
#string

n = int(input('Digite um número de 0 a 9999: '))
un = n // 1 % 10
de = n // 10 % 10
ce = n // 100 % 10
mi = n // 1000 % 10
print('Analisando....')
print('Unidade; {}'.format(un))
print('Dezena: {}'.format(de))
print('Centena: {}'.format(ce))
print('Milhar: {}'.format(mi))
#matematicamente
#Corrigido
