import os
import random

def limparTela():
    os.system("cls")

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def limparLetras(item):
    return item.upper().replace(" ","")

def addLetra(chute, letrasTentadas):
    if not chute in letrasTentadas:
        letrasTentadas.append(chute)
    else:
        print("Você já tentou esta letra!")

def verificaLetra(palavra):
    while not palavra.isalpha():
        print("\nErro, informe apenas letras!\n")
        palavra = str(input("Informe a palavra Chave: "))
    return palavra.upper()

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print (" |      (_)   ")
        print (" |       |    ")
        print (" |            ")
        print (" |            ")

    if(erros == 2):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 3):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()