import json

#Dicionario
carros_dict = {
    "marca": "honda",
    "modelo": "HRV",
    "cor": "prata"
}
#Lista
carros_list = ["Honda","volkswagem","ford","fiat","chevrolet"]

#Tupla 
carros_tuple = ("Honda","volkswagem","ford","fiat","chevrolet")

carros_json = json.dumps(carros_tuple)

print(carros_json)