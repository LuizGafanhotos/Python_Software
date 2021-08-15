import sqlite3
from sqlite3 import Error

def conection_database():
    way = "C:\\Users\\renata\\Documents\\GitHub\MeuDados\\Python_Software\\Banco\\Agendinha.db"
    con = None
    try: 
        con = sqlite3.connect(way)
    except Error as ex:
        print("Não há como eu conectar minha pessoa a isso")
        print(ex)
    return con

vcon = conection_database()

vsql = """CREATE TABLE tb_contato(
            N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NOMECONTATO VARCHAR(30),
            T_TELEFONECONTATO VARCHAR(14),
            T_EMAILCONTATO VARCHAR(30)
        );"""
        
def create_table(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Tabela criada")
    except Error as ex:
        print(ex)



create_table(vcon,vsql)
vcon.close()
