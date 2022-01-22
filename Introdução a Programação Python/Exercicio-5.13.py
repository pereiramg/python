# Escreva um programa que pergunte o valor inicial de uma divida
# e o juro mensal. Pergunte também o valor mensal que será pago.
# Imprima o numero de meses que a divida seja paga, o total pago e
# o total de juros pago.

divida = float(input("Qual o valor inicial da divida? "))
juros = float(input("Qual a taxa de juros da divida ao mês? "))
pagamento = float(input("Qual o valor de aporte mensal? "))

x = 1
JurosPago = 0
dividaInicial = divida

while divida >= pagamento :
    divida = ((juros / 100) * divida) + divida - pagamento
    print(divida)
    JurosPago = ((juros / 100) * divida) + JurosPago
    print(JurosPago)
    x += 1

print(f"A quantidade de meses pagando a divida foi: {x}")
print(f"O valor total pago foi: {dividaInicial + JurosPago}")
print(f"O total de juros pagos foi: {JurosPago}")

