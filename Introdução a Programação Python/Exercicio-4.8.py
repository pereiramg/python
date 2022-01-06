# Escreva um programa que leia dois números e que pergunte qual operação você
# deseja realizar. Você deve poder calcular soma (+), subtração (-),
# multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

numero1 = float(input("Insira um numero para calculo "))
numero2 = float(input("Insira o segundo numero para calculo "))

print("Insira qual numero deseja de operação matematica deseja fazer: ")
print(" 1 - soma (+) | 2 - subtração (-) | 3 - multiplicação (*) | 4 divisão (/)")
operacao = int(input("Qual operação matematica deseja realizar? "))

if operacao == 1:
    resultado = numero1 + numero2
elif operacao == 2:
    resultado = numero1 - numero2
elif operacao == 3:
    resultado = numero1 * numero2
elif operacao == 4:
    resultado = numero1 / numero2
else:
    print("Categoria inválida, digite um valor entre 1 e 4!")
    resultado = 0
print(f"O resultado do calculo é: {resultado:4.2f}")