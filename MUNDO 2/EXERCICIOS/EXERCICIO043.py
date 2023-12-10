#Desenvolva uma lógica que leia o peso e a altura de uma pessoa. 
#Calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: 
#- Abaixo de 18.5: Abaixo do peso 
#- Entre 18.5 e 25: Peso ideal 
#- 25 até 30: Sobrepeso 
#- 30 até 40: Obesidade 
#- acima de 40: Obesidade mórbida

#blibliotecas

from time import sleep

#Cabecalho
print('-'*4, 'BEM-VIND@ AO IMC CALCULATOR', '-'*4)
pe = float(input('Digite seu peso. EX: 1.35\n'))
sleep(1)
al = float(input('Digite sua altura: '))
sleep(1)
print('Processando...')
sleep(2)
#Calculo
imc = (pe / (al * al))
#Apresentação
print(f'Seu IMC é {imc:.2f}')
if imc < 18.5:
    print('Você está abaixo do peso. Seu IMC deve ser maior que 18.5')
elif imc > 18.5 and imc < 26:
    print('Seu peso é ideal. Continue assim!')
elif imc > 26 and imc < 31:
    print('Você está com Sobrepeso. Alivie nos alimentos.')
elif imc > 31 and imc < 41:
    print('Você Já é OBESO!!! Procure se tratar')
elif imc > 41:
    print('Obesidade Mórbida! PROCURE UM MÉDICO E.... NÃO COME MAIS PORRAAA')
