cat1= int(input('Informe o valor do cateto oposto:'))
cat2= int(input('Informe o valor do cateto adjacente:'))

hip= (cat1**2 + cat2**2)**(1/2)

#print('A Hipotenusa entre cateto oposto {} e cateto adjacente {} é igual {:.2f} '.format(cat1,cat2,hip))
print('O resultado da Hipotenusa entre os catetos informados é {:.2f}'.format(cat1,cat2,hip))
