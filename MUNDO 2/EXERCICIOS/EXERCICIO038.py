#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior O Segundo valor é maior - Não existe valor maior os dois são iguais.

n1 = int(input('Digite um número qualquer: '))
n2 = int(input('Digite outro: '))
if n1 > n2:
    print(f'{n1} é maior que {n2}!')
elif n2 > n1:
    print(f'{n2} é maior que {n1}')
else:
    print('Não existe valor maior. Pois eles são iguais!')

#Corrigido
