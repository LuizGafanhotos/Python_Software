nome = "teste.txt"
file = open("C:/Users/renata/Documents/GitHub/MeuDados/Python_Software/programas em python/" + nome, "at")
txt = input("Digite algo: ")
file.write(txt+"\n ")

file.close()
# r read - ler
# a append - anexar
# w write - escrever
# x create - criar 
# t texto
# b binário
