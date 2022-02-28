# Escreva um programa que exiba uma lista de opções (menu), adição,
# subtração, divisão, multiplicação e sair. Imprima a tabuada da operação 
# escolhida.
# Repita até que a opção saída seja escolhida.


while True:
    tabuada = int(input("Qual numero vamos utilizar na tabuada? "))
    print("Selecione a operação matematica que deseja executar: ")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")
    print("5 - Sair")
    opcao = int(input("Selecione o número: "))

    if opcao == 1:
        numero = 1
        while numero <=10:
            print(f"{tabuada} + {numero} = {tabuada + numero}")
            numero += 1
    if opcao == 2:
        numero = 1
        while numero <=10:
            print(f"{tabuada} + {numero} = {tabuada - numero}")
            numero += 1
    if opcao == 3:
        numero = 1
        while numero <=10:
            print(f"{tabuada} + {numero} = {tabuada / numero}")
            numero += 1
    if opcao == 4:
        numero = 1
        while numero <=10:
            print(f"{tabuada} + {numero} = {tabuada * numero}")
            numero += 1
    if opcao == 5:
        print("Saindo do programa")
        break
    