from funcoes import chute, limparTela, inicializa_letras_acertadas,limparLetras

limparTela()

print("Jogo da Forca\n")

desafiante = input("\nInsira o nome do desafiante: ")
competidor = input("\nInsira o nome do competidor: ")
limparTela()

palavra = input("Informe a Palavra Chave: ")

dicaA = input("\nInforme a Dica 1: ")
dicaB = input("Informe a Dica 2: ")
dicaC = input("Informe a Dica 3: ")

limparTela()

palavra = limparLetras(palavra)
listChave = []
dicas = [dicaA, dicaB, dicaC]
letrasTentadas = []
dicasPedidas = 0
erros = int(0)

for letra in palavra:
    listChave.append(letra)

letras_acertadas = inicializa_letras_acertadas(palavra)
print()
print('   '.join(letras_acertadas))


while True:
    if ("_" not in letras_acertadas):
        print("ganhou")
        print(f"Palavra: {palavra} – Vencedor: Competidor {competidor}, Desafiante: {desafiante}")
        break
    if erros == 5:
        print(f"Palavra: {palavra} – Vencedor: Desafiante: {desafiante}, Competidor {competidor}")

    print("\nEscolha uma das opções:")
    print("(1) Jogar")
    print("(2) Solicitar Dica\n")
    escolha = str(input(""))
    limparTela()

    if escolha == "1":
        chute(letrasTentadas,listChave,letras_acertadas)
        erros +=1
        
    elif escolha == "2":
        if dicasPedidas < 3:
            print(f"Dica {dicasPedidas+1}: {dicas[dicasPedidas]}")
            dicasPedidas +=1
            chute(letrasTentadas,listChave,letras_acertadas)
        else:
            print("Você não possui mais dicas!")
    else:
        print("Nenhuma das opções selecionadas.")
        continue
  
    

"""
while erros <5:
    if ("_" not in letras_acertadas):
        print("ganhou")
        break
    else:
        chute = (input("Chute uma letra: "))
        chute = limparLetras(chute)

        if (chute in listChave)==True:
            index = 0 
            for letra in listChave:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
            print('   '.join(letras_acertadas))
        else: print("Errou!");erros += 1"""


        

        
