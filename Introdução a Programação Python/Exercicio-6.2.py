# Faça um programa que leia duas listas e que gere uma terceira
# com os elementos das duas primeiras

from pickle import TRUE


print("Juntar listas\n")

lista1 = []
lista2 = []
lista3 = []

while TRUE:
    valorA = int(input("Insira os valores da primeira lista (0 para sair): "))
    if valorA == 0:
        break
    lista1.append(valorA)

while TRUE:
    valorB = int(input("Insira os valores da segunda lista (0 para sair): "))
    if valorB == 0:
        break
    lista2.append(valorB)

lista3.extend(lista1)
lista3.extend(lista2)

x = 0
while x < len(lista3):
    print(lista3[x])
    x += 1
