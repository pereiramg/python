# Variaveis String
a = "ABCDEF"
print (a[0])
print (a[5])
print (a[2])
print (len(a))

# Concatenação 
# Somente usado com strings
s = "ABC"
print (s + "C")
print (s + "D" * 5)
print ("X" + "-" * 10 + "X")
print (s + "x4 = " + s * 4)

# Composição
X = 10
print ("Joao tem %d anos" % X)

idade = 22
print ("[%d]" % idade)
print ("[%03d]" % idade)
print ("[%3d]" % idade)
print ("[%-3d]" % idade)


# Estamos imprimindo um numero decimal de cinco posições
# sendo que duas são para a parte decimal
print ("%5.2f" % 5)
print ("%5f" % 5)
print ("%s tem %d anos e apenas R$%5.2f no bolso" % ("João", 22, 51.34))

nome = "João"
idade = 22
grana = 51.34
print ("%s tem %d anos e R$%f no bolso." % (nome, idade, grana))
print ("%12s tem %3d anos e R$%5.2f no bolso." % (nome, idade, grana))
print ("%12s tem %03d anos e R$%5.2f no bolso." % (nome, idade, grana))
print ("%-12s tem %-3d anos e R$%-5.2f no bolso." % (nome, idade, grana))

# O metodo mais utilizado hoje
print ("\nO metodo mais utilizado hoje")
nome = "João"
idade = 22
grana = 51.34
print ("{} tem {} anos e R${} no bolso.".format(nome, idade, grana))
print ("{:>12s} tem {:3} anos e R${:5.2f} no bolso.".format(nome, idade, grana))
print ("{:>12s} tem {:03} anos e R${:5.2f} no bolso.".format(nome, idade, grana))
print ("{:<12s} tem {:<3} anos e R${:5.2f} no bolso.".format(nome, idade, grana))

#Surgimento do metodo F-STRING, o mais recente
print ("\nSurgimento do metodo F-STRING, o mais recente")
nome = "João"
idade = 22
grana = 51.34
print (f"{nome} tem {idade} anos e R${grana} no bolso.")
print (f"{nome:>12} tem {idade:3} anos e R${grana:5.2f} no bolso.")
print (f"{nome:>12} tem {idade:03} anos e R${grana:5.2f} no bolso.")
print (f"{nome:<12} tem {idade:<3} anos e R${grana:5.2f} no bolso.")

#Fatiamento de strings
print ("\nFatiamento de strings")
s = "ABCDEFGHI"
print (s[0:2])
print (s[1:2])
print (s[2:4])
print (s[0:5])
print (s[1:8])

#Na forma negativa ele começa a contar da direita para a esquerda
#O primeiro campo é onde começa, sempre é 0
# O segundo campo onde termina, mas sempre omite o numero atual, exemplo:
# Se termina até o 6 ele exibe até o 5, na forma negativa começa no -1 em vez do 0
print ("\n")
print (s[:2])
print (s[1:])
print (s[0:-2])
print (s[:])
print (s[-1:])
print (s[-5:7])
print (s[-2:-1])

# Sequências de tempo
print ("\nSequências de tempo")
divida = 0
compra = 100
divida = divida + compra
compra = 200
divida = divida + compra
compra = 300
divida = divida + compra
compra = 0
print(divida)

# Entrada de dados
print ("\nEntrada de dados")

x = input("Digite um numero: ")
print(x)

nome = input("Digite seu nome: ")
print(f"Você digitou {nome}")
print(f"Olá, {nome}")

anos = int(input("Anos de serviço: "))
valor_por_ano = float(input("Valor por ano: "))
bonus = anos * valor_por_ano
print(f"Bonus de R$ {bonus:5.2f}")



