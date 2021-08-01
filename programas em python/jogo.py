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
            print("Jogada Inválida")
            os.system("pause")
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

def verifyVictory():
    global velha
    vitoria="N"
    simbolos=["X","O"]
    for s in simbolos:
        vitoria="N"
        #Verificar Linhas
        il=ic=0
        while il<3:
            soma=0
            ic=0
            while ic<3:
                if velha[il][ic]==s:
                    soma += 1
                ic+=1
            if soma == 3:
                vitoria=s
                break
        if vitoria != "N":
            break
        vitoria="N"
        #Verificar Colunas
        il=ic=0
        while ic<3:
            soma=0
            ic=0
            while il<3:
                if velha[il][ic]==s:
                    soma += 1
                ic+=1
            if soma == 3:
                vitoria=s
                break
            ic+=1
        if vitoria != "N":
            break
        vitoria="N"
        #Verificação de diagonal 1
        soma=0
        idiagl=0
        idiagc=2
        while idiagc>=0:
            if velha[idiagl][idiagc]==s:
                soma+=1
            idiagl+=1
            idiagc-=1
        if soma == 3:
            vitoria=s
            break
    return vitoria
        
def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
    jogadas = 0
    quemJoga = 2
    maxJogadas = 9
    vit = "n"
    velha = [
        [" ", " ", " "], #L0C0  L0C1 L0C2
        [" ", " ", " "], #L1C0  L1C1 L0C2
        [" ", " ", " "] #L2C0  L2C1 L2C2

    ]
        
while jogarNovamente == "s":      
    while True:
        tela()
        jogoJoga()
        cpuJoga()
        tela()
        vit=verifyVictory()
        if vit != "N" or jogadas>= maxJogadas:
            break

    print(Fore.RED + "FIM DE JOGO" + Fore.YELLOW)
    if vit == "X" or vit == "O":
        print("Resultado: Jogador " + vit + " Venceu")
    else:
        print("Resultado: Empate")
        jogarNovamente = input(Fore.BLUE + "Jogar Novamente?[s/n]:  " + Fore.RESET)
        redefinir()

        