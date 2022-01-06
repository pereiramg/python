# Escreva um programa que pergunte a distancia que um passageiro
# deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km
# para viagens de até de 200 km, e R$ 0,45 para viagens mais longas

distancia = int(input("Qual distancia deseja percorrer KM? "))

if distancia >= 200 :
    valor = float(distancia * 0.50)
else :
    valor = float(distancia * 0.45)

print(f"O custo de sua viagem é {valor:4.2f}")