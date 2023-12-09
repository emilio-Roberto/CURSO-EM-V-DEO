#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Digite o tamanho da 1º reta: '))
r2 = float(input('Digite o tamanho da 2º reta: '))
r3 = float(input('Digite o tamanho da 3º reta: '))
if r1 + r2 == r3 or r1 + r3 == r2 or r3 + r2 == r1:
    print('Essas retas podem formar um triângulo!')
else:
    print('Essas retas não podem formar um triângulo')
    