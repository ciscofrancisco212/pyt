# Programa criado método Cisco

import os
os.system('cls')

print("--- Calculadora de Média Aritmética ---")
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
m = (n1 + n2) / 2
print('A média aritmética entre {} e {} é: {}'.format(n1, n2, m))