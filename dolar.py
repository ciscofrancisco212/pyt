# Lê o valor em reais que a pessoa tem na carteira
reais = float(input("Quanto dinheiro você tem na carteira? R$ "))

# Define a cotação do dólar
cotacao_dolar = 5.49

# Calcula quantos dólares ela pode comprar
dolares = reais / cotacao_dolar

# Exibe o resultado formatado com duas casas decimais
print(
    f"Com R$ {reais:.2f}, você pode comprar US$ {dolares:.2f} (considerando o dólar a R$ {cotacao_dolar})."
)
input('Sucesso! - Fim de conversão - tecle ENTER')