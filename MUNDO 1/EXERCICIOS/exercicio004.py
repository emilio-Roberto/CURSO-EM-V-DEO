#Faça um programa que leia algo pelo teclado e mostre na tela,
#seu tipo primitivo e todas as informações possiveis sobre ele.

#Meu
va = input('Digite algo; ')
print('Está em Maiúsculo ? {}\n Está em AlfaNúmerico ? {}\n Está em Númerico ? {}\n Está em Alfa ? {}\n È Decimal ? {}\n Tem Espaço ? {}'.format(va.isupper(), va.isalnum(), va.isalnum(), va.isalpha(), va.isdecimal(), va.isspace()))

#Correção
a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaço ? ', a.isspace())
print('É um número ? ', a.isnumeric())
print('É alfabético ? ', a.isalpha())
print('É alfanúmerico ? ', a.isalnum())
print('Está em maiúsculas ? ', a.isupper())
print('Está em minúsculas ? ', a.islower())
print('Está capitalizada ? ', a.istitle())

