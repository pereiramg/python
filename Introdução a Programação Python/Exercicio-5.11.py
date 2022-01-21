# Escreva um programa que pergunte o depósito inicial e a taxa de 
# juros de uma poupança. Exiba os valores mês a mês para os 24
# primeiros meses. Escreva o total ganho com juros no período.

deposito = float(input("Qual o valor inicial de deposito? "))

juros = float(input("Qual a taxa de juros da poupança no mês? "))

x = 1
while x <= 24 :
    deposito = ((juros / 100) * deposito) + deposito
    print(f"O valor do mes {x} é {deposito}")
    x += 1
