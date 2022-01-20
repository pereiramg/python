# Modifique o programa anterior de forma que o usuario também digite
# o inicio e o fim da tabuada, em vez de começar com 1 e 10

tabuada = int(input("Tabuada de: "))
inicio = int(input("Onde deseja que começe a tabuada? "))
fim = int(input("Onde deseja que termine a tabuada? "))

while inicio <= fim:
    print(tabuada * inicio)
    inicio += 1

