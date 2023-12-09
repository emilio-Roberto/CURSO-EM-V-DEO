#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: 
#- Se ele ainda vai se alistar ao serviço militar. 
#- Se é a hora de se alistar 
#- Se ele ja passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

#ADD seleção de sexo

n = int(input('Digite o ano em que você nasceu: '))
i = (2023 - n)
if i == 18:
    print('Está na hora de se alistar!!')
if i < 18:
    fal = (18 - i) 
    print(f'Ainda não está na hora de se alistar.\nFaltam {fal} anos.')
if i > 18:
    print('Já passou do tempo de se alistar.')
    sob = (i - 18)
    print(f'Você está atrasado!!\nDeveria ter se alistado a {sob} anos atrás!')

#Rsolução

'''
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual})
if idade == 18:
    print('Você tem que se alistar AGORA!!!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltarm {saldo} para o alistamento')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter ser alistado há {saldo} anos.')
'''

#Corrigido
