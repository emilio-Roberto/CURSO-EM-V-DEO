#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

cit = str(input('Digite o nome de uma cidade qualquer: ')).strip()
fat = cit.split()
print('Santo' in fat[0].upper())#passei sufoco porque coloquei 1 ao inves de 0
#Corrigido

#ou

'''cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'Santo') 
'''