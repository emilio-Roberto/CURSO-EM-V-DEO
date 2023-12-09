#Condição Simples:
n = str(input('Qual é o seu nome ? '))
if n == 'Emílio':
    print('Que nome bonito!')
print('Tenha um bom dia, {}!'.format(n))

#Estrutura Condicional Composta:
n = str(input('Qual é o seu nome ? '))
if n == 'Emílio':
    print('Que nome bonito!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(n))

#Estrutura condicional Aninhada:
n = str(input('Qual é o seu nome ? '))
if n == 'Emílio':
    print('Que nome bonito!')
elif n == 'Pedro' or n == 'Maria' or n == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif n == 'Evelly' or n == 'Angélica' or n == 'Jazilma' or n == 'Elizangela' or n == 'Carla':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(n))
