# Escreva um programa que leia um numero e verifique se é ou não um
# número primo. Para fazer essa verificação, calcule o resto da divisão
# do número por 2 e depois por todos os números ímpares até o número lido.
# Se o resto de uma dessas divisões for igual a zero, o número não é primo.
# Observe que o 0 e 1 não são primos e que 2 é o único número primo que é par.

print("Programa para busca de numeros Primos")

buscaPrimo = int(input("Insira o numero para validar se é primo "))

restoPar = buscaPrimo % 2
impar = 3

if restoPar != 0:
    while buscaPrimo > impar:
        restoImpar = buscaPrimo % impar
        if restoImpar == 0:
            print(f"O numero {buscaPrimo} não é primo")
            break
        impar += 2
    if restoImpar != 0:
        print(f"O numero {buscaPrimo} é primo")
else:
    print(f"O numero {buscaPrimo} não é primo")
