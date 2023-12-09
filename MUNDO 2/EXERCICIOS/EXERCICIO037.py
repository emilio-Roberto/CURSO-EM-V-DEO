#Escreva um programa que leia um número inteiro qualquer e
#peça para o usuário escolher qual será a base de conversão:
#1 - Binário 
#2 - Octal 
#3 - Hexadecimal.

n = int(input('Digite um número: '))
op = int(input('Escolha a sua transformação:\n1- Binário\n2- Octal\n3- Hexadecimal\nO que seja fazer ? '))
if op == 1:
    bina = str(bin(n))#Try bina = str(bin(n)[2:])
    print(bina)
elif op == 2:
    ot = str(oct(n))
    print(ot)
elif op == 3:
    ex = str(hex(n))
    print(ex)

#Corrigido
