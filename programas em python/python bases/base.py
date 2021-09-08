import os
import sqlite3
from sqlite3 import Error

#Conexão
def conection():
    way = "C:\\Users\\renata\\Documents\\GitHub\\MeuDados\\Python_Software\\Banco\\Agendinha.db"
    con = None
    try:
        con = sqlite3.connect(way)
    except Error as ex:
        print(ex)
    return con

vcon = conection()

def menu_delicia():
    options = ("Inserir Novo registro", 
                "Deletar Registro", 
                "Atualizar Registro", 
                "Consultar registro por ID", 
                "Consultar registro por Nome",
                "sair")
    cont = 1
    cont2 = 0
    os.system("cls")
    while cont < 7:
        print(f"{cont} - {options[cont2]}")
        cont += 1
        cont2 += 1

def menuInserir():
    print("imprime meu pau aqui")

def menuDeletar():
    print("oi 2.0")

def menuAtualizar():
    print("oi 2")


def menuConsultarID():
    print("oi")


def menuConsultarNOMES():
    print("OI men ")


opc = 0
while opc != 6:
    menu_delicia()
    opc = int(input("Digite uma opcao: "))
    if opc == 1:
        menuInserir()
        pass
    elif opc == 2:
        menuDeletar()
        pass
    elif opc == 3:
        menuAtualizar()
        pass
    elif opc == 4:
        menuConsultarID()
        pass
    elif opc == 5:
        menuConsultarNOMES()
        
    elif opc == 6:
        os.system("cls")
        print("Programa finalizado")
    else:
        os.system("cls")
        print("opcao inválida")
        os.system("pause")

os.system("pause")
