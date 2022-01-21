# Altere o programa anterior de forma a perguntar também o valor
# depositado mensalmente. Esse valor será depositado no inicio
# de cada mês, e você deve considerá-lo para o calculo de
# juros do mês seguinte

deposito = float(input("Qual o valor inicial de deposito? "))
juros = float(input("Qual a taxa de juros da poupança no mês? "))
aporteMensal = float(input("Qual o valor de aporte mensal? "))

x = 1
while x <= 24 :
    deposito = ((juros / 100) * deposito) + deposito + aporteMensal
    print(f"O valor do mes {x} é {deposito}")
    x += 1
    