import json

def line():
    print("-"*30)

with open('C:/Users/renata/Documents/GitHub/MeuDados/Python_Software/programas em python/modulação/bora json/json.json') as f:
    jogador = json.load(f)


line()
for c in jogador.items():
    print(c)

line()
for c2 in jogador.values():
    print(c2)
line()

