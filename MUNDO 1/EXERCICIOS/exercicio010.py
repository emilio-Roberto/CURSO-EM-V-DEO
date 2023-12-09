#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e 
#mostre quantos Dólares ela pode comprar.(Considerando 1$ = R$3,27)

real = float(input('Quanto você tem na carteira ? R$'))
dol = (real / 3.27)
print('Você pode adquirir U$D{:.2f}!'.format(dol))
#Corrigido