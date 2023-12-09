#Faça um programa que leia a largura e a altura de uma parede em metros, 
#calcule a sua área e a quantidade de tinta necessária para pintá-la. 
#Sabendo que cada litro de tinta, pinta uma área de 2m².
lar = float(input('Qual a largura da parede: '))
alt = float(input('Qual a Altura da parede: '))
comp = (lar * alt)
tin = (comp / 2)
print('Uma parede com {}m² de Largura, e {}m² de Altura, sua área total é de {}m². Utilizando 1L de tinta para pintar 2m², será necessário {}L para pintar a parede completamente!'.format(lar, alt, comp, tin))
#Corrigido