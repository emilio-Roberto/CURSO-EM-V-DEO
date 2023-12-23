#Crie um programa que faça o computador jogar Jokenpô com você.

#Importando Bibliotecas
from time import sleep

from random import randrange
#Iniciando programa
print('BEM-VINDO AO JOKENPO!!')
sleep(1)
p1 = str(input('Digite seu equipamento: ')).upper()#Entrada do usuário
eqp = ['Pedra', 'Papel', 'Tesoura']#Lista de equipamentos
pc = str((eqp [ randrange ( len ( eqp ))])).upper()#Escolha randomica
#Inicio da lógica
if p1 == 'PAPEL' and pc == 'PAPEL':
    print(f'PLAYER> {p1}\nPC> {pc}')
    sleep(1)
    print('Papel com Papel da em nada')
    sleep(1)
    print('EMPATE!!')

elif p1 == 'PAPEL' and pc == 'PEDRA':
    print(f'PLAYER> {p1}\nPC> {pc}')
    sleep(1)
    print('Papel cobre Pedra!')
    sleep(1)
    print('Você perdeu')

elif p1 == 'PAPEL' and pc == 'TESOURA':
    print(f'PLAYER> {p1}\nPC> {pc}')
    sleep(1)
    print('Tesoura corta papel!')
    sleep(1)
    print('Você perdeu')

elif p1 == 'PEDRA' and pc == 'PAPEL':
    print(f'PLAYER> {p1}\nPC> {pc}')
    sleep(1)
    print('Papel cobre Pedra!')
    sleep(1)
    print('Você Perdeu!')

elif p1 == 'PEDRA' and pc == 'PEDRA':
    print(f'PLAYER> {p1}\nPC> {pc}')
    sleep(1)
    print('Pedra com Pedra da em nada')
    sleep(1)
    print('EMPATE!!')

elif p1 == 'PEDRA' and pc == 'TESOURA':
    print(f'PLAYER> {p1}\nPC> {pc}')
    sleep(1)
    print('Pedra quebra Tesoura!')
    sleep(1)
    print('Você ganhou!')

elif p1 == 'TESOURA' and pc == 'PEDRA':
    print(f'PLAYER> {p1}\nPC> {pc}')
    sleep(1)
    print('Pedra quebra Tesoura!')
    sleep(1)
    print('Você perdeu')

elif p1 == 'TESOURA' and pc == 'PAPEL':
    print(f'PLAYER> {p1}\nPC> {pc}')
    sleep(1)
    print('Tesoura corta Papel!')
    sleep(1)
    print('Você ganhou')

elif p1 == 'TESOURA' and pc == 'TESOURA':
    print(f'PLAYER> {p1}\nPC> {pc}')
    sleep(1)
    print('Tesoura com Tesoura da em nada')
    sleep(1)
    print('EMPATE!!')
#FIM :)

#CORRIGIDO

#Resolução
    
'''
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
jogador = int(input('Qual é a sua jogada ? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
print('-' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-' * 11)
if computador == 0: #Computador jogou Pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador Vence!')
    elif jogador == 2:
        print('Computador Vence!')
    else:
    print('Jogada Inválida!')
    
elif computador == 1: #Computador jogou Papel
    if jogador == 0:
        print('Computador Vence')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador Vence')
    else:
    print('Jogada Inválida!')

elif computador == 2: #Computador jogou Tesoura
    if jogador == 0:
        print('Jogador Vence')
    elif jogador == 1:
        print('Computador Vence')
    elif jogador == 2:
        print('EMPATE')
    else:
    print('Jogada Inválida!')
'''
