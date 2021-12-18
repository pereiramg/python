# Escreva um programa que calcule o tempo de uma viagem de carro.
# Pergunte a distancia a percorrer e a velocidade média esperada 
# para a viagem

print("Tempo de viagem de carro")

distancia = float(input("Informe a distancia em KM: "))
velocidadeMedia = float(input("Informe a velocidade media/H: "))

tempo = distancia / velocidadeMedia

print(f"O tempo de viagem é: {tempo}")