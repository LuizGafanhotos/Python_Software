import os
carros=[]

class Carro:
    nome=""
    pot=0
    velMax=0
    ligado=False
    def __init__(self,nome,pot):
        self.nome=nome
        self.pot=pot
        self.velMax=int(pot)*2
        self.ligado=False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def info(self):
        estado = "Sim" if self.ligado == True else "Não"
        print(f"Nome: {self.nome}")
        print(f"Potência: {str(self.pot)}")
        print("Velocidade máxima: {}".format(str(self.velMax)))
        print(f"Ligado: {estado}")

def Menu():
    os.system("cls") or None
    print("1 - Novo Carro")
    print("2 - Informações do carro")
    print("3 - Excluir um Carro")
    print("4 - Ligar um carro")
    print("5 - Desligar um carro")
    print("6 - Listar os carros")
    print("7 - \033[2mSAIR DO PROGRAMA")
    print("Quantidades de carros " + str(len(carros)))
    opc = input("Digite umas das opções acima: ")
    return opc

def CriaCarro():
    os.system("cls") or None
    n = input("Nome do carro: ")
    p = input("Potência do carro")
    car = Carro(n,p)
    carros.append(car)
    print("Novo Carro criado com sucesso")
    os.system("pause")

def Informações():
    os.system("cls") or None
    nc = input("Informe o número do carro que deseja ver: ")
    try:
        carros[int((nc))].info()
    except:
        print("Carro não existe na lista")
    os.system("pause")

def ExcluirC():
    os.system("cls") or None
    nc = input("Informe o número do carro que deseja Excluir: ")
    try:
        del carros[int((nc))]
    except:
        print("Carro não existe na lista")
    os.system("pause")

def LigarC():
    os.system("cls") or None
    nc = input("Informe o número do carro que deseja Ligar: ")
    try:
        carros[int((nc))].ligar()
        print("Carro Ligado")
    except:
        print("Carro não existe na lista")
    os.system("pause")

def DesligarC():
    os.system("cls") or None
    nc = input("Informe o número do carro que deseja Desligar: ")
    try:
        carros[int((nc))].desligar()
        print("Carro Desligado")
    except:
        print("Carro não existe na lista")
    os.system("pause")

def ListarC():
    os.system("cls") or None
    p = 0
    for c in carros:
        print(str(p) + " - " + c.nome)
        p += 1
    os.system()
