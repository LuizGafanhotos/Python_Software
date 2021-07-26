t_carros = ("HRV","Golf","Nenhum")
l_carros=list(t_carros)
l_carros[2] = "Focus"
t_carros=tuple(l_carros)

for x in l_carros:
    print(x)