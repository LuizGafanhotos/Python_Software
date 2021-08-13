import os
import emoji
nome = "teste2.txt"
caminho = "C:/Users/renata/Documents/GitHub/MeuDados/Python_Software/programas em python/"

if os.path.exists(caminho+nome):
    print("O ARQUIVO EXISTE :)")
    print("Mas eu irei deletar kkkkk >:)")
    os.remove(caminho+nome)
else:
    print("O arquivo não existe ;-;")
    print("mas eu irei criar :)")
    arq = open(caminho+nome,"x")
    arq.close()