# Escreva um programa para aprovar o emprestimo bancario para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
# O valor da prestação mensal não pode ser superior a 30% do salário.
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de
# a pagar

valorCasa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o valor de seu salario? "))
parcelas = int(input("Quantas prestações iram financiar a casa? "))

limite = float(salario * 0.30)
prestacao = float(valorCasa / parcelas)

if prestacao <= limite:
    print(f"O valor do seu salario é compativel as prestações. Valor a pagar R${prestacao:4.2f}")
else:
    print("O valor do seu salario não é compativel com as prestações.")
