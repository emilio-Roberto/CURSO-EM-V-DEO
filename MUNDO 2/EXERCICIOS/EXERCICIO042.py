#Refaça o Desafio 0035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: 
#- Equilátero: todos os lados iguais 
#- Isóceles: Dois lados Iguais 
#- Escaleno: Todos os lados diferentes.

r1 = float(input('Digite o tamanho da 1º reta: '))
r2 = float(input('Digite o tamanho da 2º reta: '))
r3 = float(input('Digite o tamanho da 3º reta: '))
if r1 + r2 == r3 or r1 + r3 == r2 or r3 + r2 == r1:
    print('Essas retas podem formar um triângulo!')
    if r1 == r2 and r2 == r3:
        print('Esse triângulo é Equilátero.')
    elif r1 == r2 and r2 == r3 and r1 == r3:
        print('Esse triângulo é Isóceles.')
    elif r1 != r2 and r2 != r3:
        print('Esse triângulo é Escaleno.')
else:
    print('Essas retas não podem formar um triângulo.')
    if r1 == r2 and r2 == r3 and r1 == r3:
        print('Mas ele seria Isóceles.')
    elif r1 == r2 and r2 == r3 and r1 == r3:
        print('Mas ele seria Escaleno.')
    elif r1 == r2 and r2 == r3:
        print('Mas ele seria Equilátero.')
        