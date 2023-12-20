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
    print('Pedra vence papel!')
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
    print('Pedra rasga Papel!')
    sleep(1)
    print('Você ganhou!')

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
