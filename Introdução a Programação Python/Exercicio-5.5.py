# Reescreva o programa anterior para escrever os 10 primeiros multiplos de 3


fim = int(input("Digite o último número a imprirmir: "))
x = 0
y = 1
while x <= fim and y <=10:
    if x % 3 == 0:
        print(x)
        y += 1
    x += 1
