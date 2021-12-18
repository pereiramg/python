# Faça um programa que calcule o aumento de um salario.
# Ele deve solicitar o valor do salario e a porcentagem do aumento.
# Exiba o valor do aumento e do novo salário.

print("Calculo de aumento de salário")

salario = float(input("Informe o valor do salario: "))
porcentagem = float(input("Informe a porcentagem de aumento: "))

calculo = (salario * porcentagem) / 100
novoSalario = salario + calculo

print(f"O valor de aumento do seu salario é: {calculo:5.2f}")
print(f"O valor do seu novo salario é: {novoSalario:5.2f}")

