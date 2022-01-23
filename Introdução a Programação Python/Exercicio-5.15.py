# Escreva um programa para controlar uma pequena máquina registradora.
# Você deve solicitar ao usuário que digite o código do produto
# e a quantidade comprada. Utilize a table de código a seguir para
# obter o preço de cada produto:

# codigo     preço
# 1           0,50
# 2           1,00
# 3           4,00
# 5           7,00
# 9           8,00

# Seu programa deve exibir o total das compras depois que o usuário
# digitar 0. Qualquer outro código deve gerar a mensagem de erro
# "Código inválido"

codigo1 = codigo2 = codigo3 = codigo5 = codigo9 = 0


while True :
    codigo = int(input("Digite o codigo de compra ou 0 para sair: "))
    if codigo == 0 :
        break
    quantidade = int(input("Digite a quantidade comprada: "))
    if codigo == 1 :
        codigo1 += 0.50 * quantidade
    elif codigo == 2 :
        codigo2 += 1.00 * quantidade
    elif codigo == 3 :
        codigo3 += 4.00 * quantidade
    elif codigo == 5 :
        codigo5 += 7.00 * quantidade
    elif codigo == 9 :
        codigo9 += 8.00 * quantidade
    else :
        print("Codigo invalido")
soma = codigo1 + codigo2 + codigo3 + codigo5 + codigo9
print(f"O valor total de suas compras foi {soma}")
