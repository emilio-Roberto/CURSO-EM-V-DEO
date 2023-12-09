#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, 
#de acordo com a idade:
#-Até 9 anos: mirim
#-Até 14 anos: Infantil 
#- Até 19 anos: Junior 
#- Até 20 anos: Sênior 
#- Acima de 20 anos: Master.

i = int(input('Digite sua idade: '))
mir = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
inf = [10, 11, 12, 13, 14]
jun = [15, 16, 17, 18, 19]
sen = [20, 21, 22, 23, 24, 25]
mas = [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40] 
if i <= 9:
    print('Sua categoria é Mirim.')
elif i in inf:
    print('Sua categoria é infantil.')
elif i in jun:
    print('Sua categoria é Junior.')
elif i in sen:
    print('Sua categoria é Senior.')
elif i in mas:
    print('Sua categoria é Master.')
else:
    print('Desculpe, o limite é 40 anos!')

#Corrigido

#RESOLUÇÂO

'''
from datetime import date

atual = date.today().year
nascimento = int(input('Ano de Nascimento: ))
idade = atual - nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')
'''
