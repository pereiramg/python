# Escreva um programa que leia dois números. 
# Imprima o resultado da multiplicação do primeiro pelo segundo. 
# Utilize apenas os operadores de soma e subtração 
# para calcular o resultado. Lembre-se de que podemos entender a multiplicação
# de dois numeros como somas sucessivas de um deles.
# Assim, 4 x 5 = 5+5+5+5 = 4+4+4+4+4

numero1 = int(input("Insira o primeiro valor: "))
numero2 = int(input("Insira o segundo valor "))

x = 1
resultado = 0
while x <= numero1 :
    resultado += numero2
    x += 1

print(f"O valor da multiplicação é: {resultado}")

