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

def query(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Operação realizada com bronha com sucesso")
        conexao.close()

def consultar(conexao,sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    #conexao.close()
    return res

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
    os.system("cls")
    vid = int(input("Digite um id: "))
    vnome = input("Digite o nome: ")
    vtelefone = input("Digite o telefone: ")
    vemail = input("Digite o email: ")

    vsql = f"INSERT INTO tb_contato2 VALUES ('{vid}', '{vnome}', '{vtelefone}', '{vemail}')"
    query(vcon,vsql)

def menuDeletar():
    os.system("cls")
    vid = input("Digite o ID do registro a ser deletado: ")
    vsql="DELETE FROM tb_contato2 WHERE N_IDCONTATO="+vid
    query(vcon,vsql)

def menuAtualizar():
    os.system("cls")
    vid = input("Digite o ID do registro a ser alterado: ")
    r = consultar(vcon,"SELECT * FROM tb_contato2 WHERE N_IDCONTATO="+vid)
    rnome = r[0][1]
    rtelefone = r[0][2]
    remail = r[0][3]
    vnome = input("Digite o nome: ")
    vtelefone = input("Digite o telefone: ")
    vemail = input("Digite seu email: ")
    if (len(vnome) == 0):
        vnome = rnome
    if(len(vtelefone)==0):
        vtelefone = rtelefone
    if(len(vemail)==0):
        vemail = remail
    vsql = "UPDATE tb_contato2 SET T_NOMECONTATO='"+vnome+"',T_TELEFONECONTATO='"+vtelefone+"',T_EMAILCONTATO='"+vemail+"' WHERE N_IDCONTATO="+vid
    query(vcon,vsql)


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
    elif opc == 2:
        menuDeletar()
    elif opc == 3:
        menuAtualizar()
    elif opc == 4:
        menuConsultarID()
    elif opc == 5:
        menuConsultarNOMES()
        
    elif opc == 6:
        os.system("cls")
        print("Programa finalizado")
    else:
        os.system("cls")
        print("opcao inválida")
        os.system("pause")


vcon.close()
os.system("pause")
