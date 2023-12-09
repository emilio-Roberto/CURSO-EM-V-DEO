#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Digite um valor em Metros a ser convertido: '))
km = (m / 1000)
hm = (m / 100)
dam = (m / 10)
dm = (m * 10)
cm = (m * 100)
mm = (m * 1000)
print('{}m equivale a:\n{:.0f}cm,\n{:.0f}mm,\n{:.0f}dm,\n{}dam,\n{}hm,\n{}km.'.format(m, cm, mm, dm, dam, hm, km))
#Corrigido