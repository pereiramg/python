# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule
# quantos dias de vida um fumante perderá.
# Exiba o total em dias

print("calcular a redução do tempo de vida de um fumante")

cigarros = int(input("Informa quantidade de cigarros fumados por dia: "))
anos = int(input("Quantos anos já fumou? "))

totalMinutos = (cigarros * 10) * (anos * 365)
minutosParaDias = (totalMinutos / 60) / 24

print(f"A quantidade de dias perdido com o cigarro é: {minutosParaDias}")