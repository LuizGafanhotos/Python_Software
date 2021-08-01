import os
import random
from colorama import Fore, Back, Style

jogarNovamente = "s"
jogadas = 0
quemJoga = 2
maxJogadas = 9
vit = "n"
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]

]
def tela():
    linha = "-"
    global velha
    global jogadas
    os.system("cls")
    print("   0   1   2")
    print("0: " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print(f"   {linha*11}")
    print("1: " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print(f"   {linha*11}")
    print("2: " + velha[2][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("Jogadas: "+ Fore.GREEN + str(jogadas) + Fore.RESET)

def jogoJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 2 and jogadas < maxJogadas:
        l = int(input("Linha..: "))
        c = int(input("Coluna.: "))
        try:
            l = int(input("Linha..: "))
            c = int(input("Coluna.: "))
            while velha[l][c] != " ":
                l = int(input("Linha..: "))
                c = int(input("Coluna.: "))
            velha[l][c] = "X"
            quemJoga = 1
            jogadas += 1
        except:
            print("Linha ou coluna inválida")
            # vit="n"
            
def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 1 and jogadas < maxJogadas:
        l = random.randrange(0,3)
        c = random.randrange(0,3)
        while velha[l][c] != " ":
            l = random.randrange(0,3)
            c = random.randrange(0,3)
        velha[l][c] = "O"
        jogadas+=1
        quemJoga=2

while True:
    tela()
    jogoJoga()
    cpuJoga()