#Escreva um programa que leia a velocidade de um carro.
#se ele ultrapassar 80Km/h. Mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7.00 por cada Km acima do limite.

vel = int(input('Digite a velocidade em Km/h do veiculo: '))
if vel > 80:
    print('Você foi multado!!')
    if vel > 80:
        excess = (vel - 80)
        cal = (excess * 7)
    print('O excesso de velocidade foi +{}Km/h.\nSua multa será aplicada no valor de R$7.00 por Km/h.\nValor da multa: R${:.2f}'.format(excess, cal))
else:
    print('Velocidade permitida na via, você não será multado!')
#Corrigido

#ou

'''vel = int(input('Digite a velocidade em Km/h do veiculo: '))
if vel > 80:
    print('Você foi multado!!')
    if vel > 80:
        excess = (vel - 80)
        cal = (excess * 7)
    print('O excesso de velocidade foi +{}Km/h.\nSua multa será aplicada no valor de R$7.00 por Km/h.\nValor da multa: R${:.2f}'.format(excess, cal))
print('Velocidade permitida na via, você não será multado!')
'''