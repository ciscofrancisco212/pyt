import os
os.system('cls')
n1= int(input("Digite o primeiro número: "))
n2= int(input("Digite o segundo número: "))

s= n1 + n2
m= n1 * n2
d= n1/n2
di= n1//n2
r= n1%n2 
e= n1**n2

print('A soma é {}, \n o produto é {}, e a \n divisão é {}'.format(s, m, d), end=' ')
print('A divisão inteira é {}, o resto da divisão é {}, e a potência é {}'.format(di, r, e))
