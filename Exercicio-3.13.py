# Escreva um programa que converta uma temperatura digitada em ºC
# em ºF. A formula para essa conversão é: F = (9 * c) / 5 + 32

print("Conversão de ºC para ºF")

celsius = float(input("Informe o valor em ºC: "))

calculo = (9 * celsius) / 5 + 32

print(f"O valor de consersão é: {calculo:5.2f}")
