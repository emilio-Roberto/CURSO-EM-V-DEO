#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = ((n1 + n2) / 2)
print('Com as notas {} e {}, média do aluno é {:.1f}'.format(n1, n2, m))
#Corrigido