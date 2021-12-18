# Faça um programa que solicite o preço de uma mercadoria e o percentual
# de desconto. Exiba o valor do desconto e o preço a pagar

print("Desconto em mercadoria")

precoProduto = float(input("Informe o valor da mercadoria: "))
desconto = float(input("Informe o valor de desconto: "))

valorDesconto = (precoProduto * desconto) / 100
valorProduto = precoProduto - valorDesconto

print(f"O valor de desconto no produto é: {valorDesconto:5.2f}")
print(f"O valor do produto final com desconto é: {valorProduto:5.2f}")
