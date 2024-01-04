#CRIE UM PROGRAMA QUE MOSTRE NA TELA TODOS OS NÚMEROS PARES QUE ESTÃO NO INTERVALO ENTRE 1 E 50.
print('No intervalo emtre 1 e 50, esses são os números PARES:')
for n in range(1, 51):#laço
    r = n % 2 #Calculo para saber se é impar ou par
    if r == 0: #Condição
        print(n) #Saída
#Corrigido
        
#Resolução
#EX1 -
'''for n in range(1, 51):
    print('.', end=' ')
    if n % 2 == 0:
        print(n, end=' ')
print('FIM')''' #Repetindo laços.

#EX2 -
'''for n in range(2, 51, 2):
    print('.', end=' ')
    print(n, end=' ')
print('FIM')''' #Reduzindo metade do processamento.
