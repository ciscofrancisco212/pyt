import os
os.system('cls')
#Programa de conversão de unidades de medida

medida = float(input('Digite o valor da medida: '))

dm= medida * 10
cm= medida * 100
mm= medida * 1000
km= medida / 1000
hm= medida / 100
dam= medida / 10

print(f'{medida} metros equivale a:')
print(f'{dm} decímetros')
print(f'{cm} centímetros')
print(f'{mm} milímetros')
print(f'{km} quilômetros')
print(f'{hm} hectômetros')
print(f'{dam} decâmetros')
