#Faça um programa que leia três números e mostre qual é o maior e qualé o menor.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Não ta travado... Digite outro número: '))
if n1 < n2 < n3:
    print('{:.0f} é o menor número dos 3.'.format(n1))
    if n2 > n3:
        print('O maior número é o {:.0f}'.format(n2))
    else:
        print('O maior número é o {:.0f}'.format(n3))

if n2 < n3 < n1:
    print('{:.0f} é o menor número dos 3.'.format(n2))
    if n1 > n3:
        print('O maior número é o {:.0f}'.format(n1))
    else:
        print('O maior número é o {:.0f}'.format(n3))

if n3 < n1 < n2:
    print('{:.0f} é o menor número dos 3.'.format(n3))
    if n2 > n1:
        print('O maior número é o {:.0f}'.format(n2))
    else:
        print('O maior número é o {:.0f}'.format(n1))
        