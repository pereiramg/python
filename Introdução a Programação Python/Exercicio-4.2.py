# Escreva um programa que pergunte a velocidade do carro de um usuário.
# Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h

velocidade = int(input("Qual a velocidade do carro? "))

if (velocidade > 80 ) :
    multa = (velocidade - 80) * 5
    print (f"Você foi multado por ultrappsar os 80 km/h e sua multa é de R$ {multa}")
