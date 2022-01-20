# Modifique o programa anterior para que aceite respostas com letras
# maiusculas e minusculas em todas as questões

pontos = 0
questao = 1

while questao <= 3 :
    respota = input(f"Resposta da questão {questao}: ")
    if questao == 1 and (respota == "b" or respota == "B") :
        pontos += 1
    if questao == 2 and (respota == "a" or respota == "A") :
        pontos += 1
    if questao == 3 and (respota == "d" or respota == "D") :
        pontos += 1
    questao +=1
print(f"O aluno fez {pontos} pontos(s)")

