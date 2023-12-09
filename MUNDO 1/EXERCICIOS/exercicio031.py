#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem. Cobrando R$0.50 por Km para viagens de até 200km e R$0.45 para viagens mais longas.

dis = float(input('Digite a distância em Kms da viagem: '))
if dis <= 200:
    print('viagens de até 200Kms são cobrados R$0.50 por KM.')
    print('Sua viagem foi de {}kms.\nEla custará R${:.2f}.'.format(dis, (0.50 * dis)))
if dis >200:
    print('viagens de até 200Kms são cobrados R$0.50 por KM.')
    print('Para viagens mais longas, o valor a ser cobrado é R$0.45')
    print('Sua viagem foi de {}kms.\nEla custará R${:.2f}.'.format(dis, (0.45 * dis)))
print('Obrigado por viajar conosco!!\nVolte sempre!')
#Corrigido

#OU

'''
'''
