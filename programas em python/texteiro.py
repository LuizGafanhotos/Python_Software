import re
from os import system
system("cls")
nome = "teste2.txt"

file = open("C:/Users/renata/Documents/GitHub/MeuDados/Python_Software/programas em python/"+nome,"rt")
res = re.sub("\s","-",file.readline())
file.close()
file = open("C:/Users/renata/Documents/GitHub/MeuDados/Python_Software/programas em python/"+nome,"wt")
file.write(res)
file.close()
print(res)