from os import error
import sqlite3
from sqlite3 import Error

def conector_banco():
    way = "C:\\Users\\renata\\Documents\\GitHub\MeuDados\\Python_Software\\Banco\\Agendinha.db"
    con = None
    try: 
        con = sqlite3.connect(way)
    except Error as ex:
        print("Não há como eu conectar minha pessoa a isso")
        print(ex)
    return con

vcon = conector_banco()
# numTelefone = int(input("Digite seu Id de contato: "))
# nome = input("Digite seu nome: ")
# telefone = input("Digite seu telefone: ")
# email = input("Digite seu email: ")


# vsql = f"INSERT INTO tb_contato VALUES ('{numTelefone}','{nome}','{telefone}','{email}');"

def inserir(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Texto inserido com sucesso")
    except Error as ex:
        print(ex)

def deletar(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro deletado")

def atualizar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro atualizado")


def consulta(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    return resultado

vsql = "SELECT * FROM tb_contato"
# vsql = "DELETE FROM tb_contato WHERE N_IDCONTATO=3"
# vsql = "UPDATE tb_contato SET T_NOMECONTATO='Bruno' WHERE N_IDCONTATO=1"

# inserir(vcon,vsql)
# deletar(vcon,vsql)
# atualizar(vcon,vsql)
res = consulta(vcon,vsql)
for r in res:
    print(r)
