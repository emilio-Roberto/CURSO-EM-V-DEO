#escreva um programa que pergunte o salário de um funcionário e cálcule o valor do seu aumento.
#Para salários superiores a R$1.250.00. Cálcule um aumento de 10%.
#Para os infeirores ou iguais, o aumento é de 15%.

sa = float(input('Digite seu salário: R$'))
cal1 = ((10 * sa) / 100)
cal2 = ((15 * sa) / 100)
if sa > 1250:
    print('Para o seu holerite, o calculo de aumento é de 10%.\nLogo, seu holerite do mês que vem será R${}'.format(cal1))
else:
    print('Para o seu holerite, o calculo de aumento é de 10%.\nLogo, seu holerite do mês que vem será R${}'.format(cal2))
