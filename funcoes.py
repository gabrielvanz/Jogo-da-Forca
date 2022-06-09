import os
import random

def limparTela():
    os.system("cls")

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def limparLetras(item):
    return item.upper().replace(" ","")

"""def tentativaChute(){

}"""

def chute(letrasTentadas,listChave,letras_acertadas):
    telaCheia = 0
    while True:
        chute = (input("Chute uma letra: "))
        chute = limparLetras(chute)
        if not chute in letrasTentadas:
            letrasTentadas.append(chute)
            #Chamar função ChuteCerto
            if (chute in listChave):
                index = 0 
                for letra in listChave:
                    if (chute == letra):
                        letras_acertadas[index] = letra
                    index += 1
                print('   '.join(letras_acertadas))
            
                
            break
        print("Você já tentou esta letra!")
        """telaCheia = telaCheia + 1
        print(telaCheia)
        if telaCheia == 4:
            limparTela()
            telaCheia = 0"""
        


    


"""
def chutesCertos():
    print()




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
        else: print("Errou!");erros += 1



        """