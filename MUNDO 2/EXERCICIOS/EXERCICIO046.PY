#FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA PARA O ESTOURO DE FOGOS DE ARTIFICIO. 
#INDO DE 10 ATÉ 0. COM UMA PAUSA DE 1 SEGUNDO ENTRE ELES.

#importando bibliotecas
from time import sleep
#inicio
s = input('Pressione enter para iniciar a contagem!')
#laço
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('🎆🎆🎆🎆🎆')
#FIM
#Corrigido

#CORREÇÃO
'''from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('BUM! BUM! POOOW!!')'''
