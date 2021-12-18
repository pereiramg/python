# Escreva um programa que pergunte a quantidade de KM percorridos por um carro
# alugado pelo usuário, assim como a quantidade de dias pelos quais o carro
# foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia
# e R$ 0,15 por KM rodado.

print("Calculo do valor de um carro alugado")

km = float(input("Informe o valor de KM percorrido: "))
dias = float(input("Informe a quantidade de dias alugado: "))

valor = (dias * 60) + (km * 0.15)

print(f"O valor total a pagar é: {valor}")