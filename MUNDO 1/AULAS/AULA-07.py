nome = input('Qual seu nome: ')
print('Prazer em te conhecer {:=^10}!'.format(nome))

n1 = input('Digite um valor: ')
n2 = input('Digite outro valor: ')
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A some é {}, \n o produto é {} e a \n  divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))

#4**(1/2) (Calculo de raiz quadrada de 4)
