#Faça um programa que leia uma frase pelo teclado e mostre: 
#-Quantas vezes aparece a letra "A". 
#-Em que posição ela aparece a primeira vez. 
#-Em que posição ela aparece a última vez.

f = str(input('Digite uma frase: ')).upper().strip()
qtd = f.count('A')
pri = f.find('A') + 1
sec = f.rfind('A') + 1
print('Na frase digitada, a letra "A" apareceu: {}'.format(qtd))
print('A primeira aparição foi na posição: {}'.format(pri))
print('A ultima aparição foi na posição: {}'.format(sec))
#Corrigido
