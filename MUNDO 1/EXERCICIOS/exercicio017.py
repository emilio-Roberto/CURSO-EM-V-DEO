#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

ca1 = float(input('Digite o cateto oposto: '))
ca2 = float(input('Digite o cateto adjacente: '))
cal = float((ca1 ** 2) + (ca2 ** 2))
ra = float((cal) ** (1/2))
#ou ra = ((ca1 ** 2 + ca2 ** 2) ** (1/2))
#ou import math - ra = math.hypot(ca1, ca2)
print('O triangulo retangulo com o cateto oposto {} e o cateto adjacente {}, tem o comprimento da hipotenusa igual a {:.2f}!'.format(ca1, ca2, ra))
#Corrigido
