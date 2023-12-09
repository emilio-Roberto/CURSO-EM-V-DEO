#Faça um programa que leia o nome completo de uma pessoa, mostrando o primeiro e o ultimo nome separadamente. 
#EX: ANA Maria Souza -Pirmiero: Ana - ultimo; Souza.

n = str(input('Digite seu nome completo: ')).strip()
no = n.split()
print('Seu primeiro nome é {} e o ultimo é {}!'.format(no[0], no[len(no)-1]))
#Corrigido
