# Faça um programa que percorra duas listas e gere uma terceira
# sem elementos repetidos.


print("Juntar listas nas repetidas\n")

lista1 = []
lista2 = []
lista3 = []

while True:
    valorA = int(input("Insira os valores da primeira lista (0 para sair): "))
    if valorA == 0:
        break
    lista1.append(valorA)

while True:
    valorB = int(input("Insira os valores da segunda lista (0 para sair): "))
    if valorB == 0:
        break
    lista2.append(valorB)

x = 0
y = 0

while x < len(lista1):
    #print("valor x", lista1[x])
    while y < len(lista2):
        #print("Valor y", lista2[y])
        if lista1[x] == lista2[y]:
            #y = 0
            break
        y += 1
        if y >= len(lista2):
            lista3.append(lista1[x])
            #print("valor lista3", lista1[x])
    x += 1

lista3.extend(lista2)

x = 0
while x < len(lista3):
    print(lista3[x])
    x += 1
