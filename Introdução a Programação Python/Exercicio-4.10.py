# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia
# elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação:
# R para residencia, I para indústrias e C para comércios.
# Calcule o preço a pagar de acordo com a table a seguir
# prelo por tipo de faixa de consumo

# residencial - até 500 - 0,40
# residencial - acima de 500 - 0,65

# comercial - até 1000 - 0,55
# comercial - acima de 1000 - 0,60

# industrial - até 5000 - 0,55
# industrial - acima de 5000 - 0,60

consumo = int(input("Qual foi a quantidade de Kwh consumido? "))
print("Qual o tipo de instalação?")
print("1 - para residencia")
print("2 - para indústrias")
print("3 - para comércios")
instalacao = int(input("Escolha as opções de 1 a 3 "))


if instalacao == 1:
    if consumo > 500:
        pagar = consumo * 0.65
    else:
        pagar = consumo * 0.40
elif instalacao == 2:
    if consumo > 5000:
        pagar = consumo * 0.60
    else:
        pagar = consumo * 0.55
elif instalacao == 3:
    if consumo > 1000:
        pagar = consumo * 0.60
    else:
        pagar = consumo * 0.55
else:
    print("Valor invalido de entrada")
    pagar = 0

print(f"O valor a pagar na sua conta de luz é R${pagar:4.2f}")
