#Crie um programa que leia duas notas de um aluno e calcule sua média, 
#mostrando uma mensagem no final, de acordo com a média atingida: 
#- Média abaixo de 5.0: Reprovado 
#- Média entre 5.0 e 6.9: Recuperação 
#- Média 7.0 ou superior: Aprovado

n1 = float(input('Digite a primeira média: '))
n2 = float(input('Digite a segunda média: '))
me = ((n1 + n2) / 2)
if me < 5.0:
    print(f'Média: {me}')
    print('Reprovado!')
elif me in range(5, 7): 
    print(f'Média: {me}')
    print('Recuperação')
elif me >= 7.0:
    print(f'Média: {me}')
    print('Aprovado')
 
#Corrigido
    
#Resolução    
'''
n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
m = ((n1 + n2) / 2)
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, m))
if 7 > m >=5:
    print('O aluno está em RECUPERAÇÃO!')
elif m < 5:
    print('O aluno está REPROVADO!')
elif m >= 7:
    print('O aluno está APROVADO!')   
'''