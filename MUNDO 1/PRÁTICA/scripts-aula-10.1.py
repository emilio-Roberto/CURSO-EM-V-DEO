'''tempo = str(input('Quantos anos tem o seu carro: '))
if tempo<='3':
    print('Seu carro é novo!')
else:
    print('Teu carro é veio!!')
print('---FIM---')'''

#OU

'''tempo = int(input('Quantos anos tem seu carro ?'))
print('carro novo' if tempo <= 3 else 'Carro velho')
print('---FIM---')
'''

#PRÁTICA:

'''n = str(input('Qual é o seu nome? '))
if n == 'Evelly':
    print('Que nome lindo você tem!')
else:
    print('Olá {}'.format(n))'''

#2.1

'''n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = ((n1+n2) / 2)
print('A sua Média foi {}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÊNS!!')
else:
    print('Sua média foi ruim... ESTUDE MAIS!!!')'''

#2.2

'''n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = ((n1+n2) / 2)
print('A sua Média foi {:.1f}'.format(m))
print('Sua média foi boa! PARABÊNS!!' if m >= 6.0 else 'Sua média foi ruim... ESTUDE MAIS!!!')'''
