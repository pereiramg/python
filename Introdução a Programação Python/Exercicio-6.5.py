# Simulação de uma fila de banco com multiplas entradas

ultimo = 10
fila = list(range(1,ultimo + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operacao = list(input("Operação (F, A ou S): "))
    
    posicao = 0
    while posicao < len(operacao):
        if operacao[posicao] == "A":
            if len(fila) > 0:
                atendimento = fila.pop(0)
                print(f"Cliente {atendimento} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao[posicao] == "F":
            ultimo += 1 # Inclementa o ticket do novo cliente
            fila.append(ultimo)
        elif operacao[posicao] == "S":
            exit()
        else:
            print("Operação invalida! Digite apenas F, A ou S!")
        posicao += 1