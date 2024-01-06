#FAÇA UM PROGRAMA QUE FAÇA A SOMA ENTRE TODOS OS NÚMEROS IMPARES QUE SÃO MÚLTIPLOS DE TRÊS E QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500.

'''print('Na sequencia entre 1 e 500, estes número snão Imapres e Multiplos por 3: ') #Apresentação
for n in range(1, 501): #Laço
        r = n % 2 # Calculo IMPAR / PAR
        if r == 1: # SE FOR IMPAR
            di = (n / 3) # Calculo multiplo DIVISÂO
            mut = (di * 3) # Calculo Multiplo MULTIPLICAÇÂO
            if mut == n: # SE FOR DIVISIVEL POR 3
                s = 
                print(s)
                 # Retorno'''

# NÂO CONSEGUI FAZER :(

# R E S O L U Ç Â O

soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))

# C O R R I G I D O