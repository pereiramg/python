# Faça um programa que leia uma expressão com parênteses.
# Usando pilhas, verifique se os parênteses foram abertos e fechados
# na ordem correta.
# Exemplo:
# (())  OK
# ()()(()())    OK
# ())   Erro
# Você pode adicionar elementos à pilha sempre que encontrar abre
# parênteses e desempilhá-la a cada fecha parêntes. Ao desempilhar, verifique se o 
# topo da pilha é um abre parênteses. Se a expressão estiver correta,
# sua pilha estará vazia no final.

parenteses = []

while True:
    print("Digite ( para adicionar pratos na pilha,")
    print("ou ) para remover os pratos. S para sair.")

    recebeValor = input("(, ), S: ")
    if recebeValor == "(" or recebeValor == ")":
        parenteses.append(recebeValor)
    elif recebeValor == "S":
        break
    else:
        print("Operação invalida! Digite apenas (, ), ou S!")

print("Validando a estrutura")

posicao = 0
adicao = 0
remocao = 0
#print(len(parenteses))
while posicao < len(parenteses):
    if parenteses[posicao] == "(":
        adicao += 1
    elif parenteses[posicao] == ")":
        remocao += 1
    
    if (posicao + 1) == len(parenteses) and parenteses[posicao] == ")":
        resultado = (adicao - remocao)
    elif (posicao + 1) == len(parenteses) and parenteses[posicao] == "(":
        resultado = 1
    posicao += 1

if resultado == 0:
    print("A pilha foi fechado sem erros")
else:
    print("A pilha foi fechado com erros")