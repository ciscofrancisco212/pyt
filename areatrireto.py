# Dado o triângulo retângulo com: Hipotenusa=10 e cateto Adjacente=8
# Calcular a área desse triângulo
print('Determine a área do triângulo Retângulo, conforme dados abaixo:')
hip= float(input('Informe o valor da Hipotenusa: '))
ca= float(input('Informe o valor do cateto Adjacente: '))

co= (hip ** 2 - ca ** 2) ** (1/2)
area= (co * ca) /2

print('Dado a hipotenusa= {} e cateto adjacente= {} O cateto Oposto é: {:.2f}\nE sua Área igual: {:.2f}'.format(hip,ca,co,area))

input('Sucesso! - tecle ENTER para sair')








