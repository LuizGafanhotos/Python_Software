import re
import os
os.system("cls") or None
texto = "Curso de tecnologia do Curso em video do youtube"
search = str(input("Pesquisar: "))
res = re.findall(search,texto)
qtde = len(res)
print(res)
print("Qtde: " + str(qtde))

for t in res:
    print(t)
