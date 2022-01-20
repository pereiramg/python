# Escreva um programa que leia dois numeros. 
# Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. 
# Utilize apenas os operadores de soma e subtração para calcular o resultado. 
# Lembre-se de que podemos entender o quociente da divisão de dois números como a 
# quantidade de vezes que podemos retirar o divisor do dividendo.
# Logo, 20 / 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20


numero1 = int(input("Insira o primeiro valor: "))
numero2 = int(input("Insira o segundo valor "))

x = 0
sobra = numero1

while sobra >= numero2 :
    sobra -= numero2
    x += 1

print(f"O valor da divisão do {numero1} / {numero2} é: {x}, e sua sobra é {sobra}")
