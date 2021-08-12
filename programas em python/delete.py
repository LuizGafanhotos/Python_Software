import os
import emoji
nome = "teste2.txt"
caminho = "C:/Users/renata/Documents/GitHub/MeuDados/Python_Software/programas em python/"

if os.path.exists(caminho+nome):
    print(emoji.emojize("O ARQUIVO EXISTE :slight_smile:"))
    print("Mas eu irei deletar kkkkk")
    os.remove(caminho+nome)
else:
    print(emoji.emojize("O arquivo não existe :cry:"))
    print(emoji.emojize("mas eu irei criar :slight_smile:"))
    arq = open(caminho+nome,"x")
    arq.close()