# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, 15%

salario = float(input("Insira o seu salario: "))

if salario > 1250 :
    novoSalario = salario * 0.10
    print(f"Seu aumento será de {novoSalario:3.2f}")

if salario <= 1250 :
    novoSalario = salario * 0.15
    print(f"Seu aumento será de {novoSalario:3.2f}")




