# Escreva um programa que leia três números e que imprima o maior e o menor

numero1 = int(input("Insira o primeiro numero: "))
numero2 = int(input("Insira o primeiro numero: "))
numero3 = int(input("Insira o primeiro numero: "))

if numero1 >= numero2 and numero1 >= numero3 :
    print(f"O numero {numero1} é o maior ou igual")

if numero2 >= numero1 and numero2 >= numero3 :
    print(f"O numero {numero2} é o maior ou igual")

if numero3 >= numero1 and numero3 >= numero2 :
    print(f"O numero {numero3} é o maior ou igual")

# Numero Menor
if numero1 <= numero2 and numero1 <= numero3 :
    print(f"O numero {numero1} é o menor ou igual")

if numero2 <= numero1 and numero2 <= numero3 :
    print(f"O numero {numero2} é o menor ou igual")

if numero3 <= numero1 and numero3 <= numero2 :
    print(f"O numero {numero3} é o menor ou igual")



