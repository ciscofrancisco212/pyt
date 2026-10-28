import os
os.system('cls')
#Programa de conversão de unidades de medida

medida = float(input('Digite o valor da medida em metros: '))

dm= medida * 10
cm= medida * 100
mm= medida * 1000
km= medida / 1000
hm= medida / 100
dam= medida / 10

print('O valor {} em metros vale \n{} em dm, {} \nem cm e {} \nem mm'.format(medida, dm, cm, mm))
print('O valor {} em metros vale \n{} em km, {} \nem hm e {} \nem dam'.format(medida, km, hm, dam))