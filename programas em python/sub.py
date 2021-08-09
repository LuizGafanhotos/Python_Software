import re

texto = "Curso de java vindo da CeV e do CBF_Cursos, ambos do youtube"

res=re.sub("\s","-",texto)

print(res)