#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
n = int(input('Digite um número: '))
print('-' * 12)
print('{} X {:2} = {}\n{} X {:2} = {}\n{} X {:2} = {}\n{} X {:2} = {}\n{} X {:2} = {}\n{} X {:2} = {}\n{} X {:2} = {}\n{} X {:2} = {}\n{} X {:2} = {}\n{} X {} = {:2}'.format(n, 1, (n*1), n, 2, (n*2), n, 3, (n*3), n, 4, (n*4), n, 5, (n*5), n, 6, (n*6), n, 7, (n*7), n, 8, (n*8), n, 9, (n*9), n, 10, (n*10)))
print('-' * 12)
#Corrigido