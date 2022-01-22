# Escreva um programa que leia números inteiros do teclado.
# O pragrama deve ler os números até que o usuário digite 0.
# No final da execução, exiba a quantidade de números digitados, assim como
# a soma e a média aritmética.

soma = 0
numeros = 0
while True :
    valor = int(input("Digite um número para a soma ou 0 para sair: "))
    if valor == 0 :
        break
    numeros += 1
    soma += valor

print(f"A quantidade de numeros digitados foi: {numeros} e sua media aritmética {soma / numeros}")