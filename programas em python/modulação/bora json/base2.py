import json

#Dicionario
carros_dict = '{"nome":"Luiz","time":"nenhum","vivo": "True","energia": 100,"mochila": ["pederneira","corda","linha","arame"],"areonave":[{"tipo":"transporte","habilidade":70},{"tipo":"defesa","habilidade":100},{"tipo":"reconhecimento","habilidade":20}]}'
#Lista
carros_list = ["Honda","volkswagem","ford","fiat","chevrolet"]

#Tupla 
carros_tuple = ("Honda","volkswagem","ford","fiat","chevrolet")

carros_json = json.dumps(carros_dict,indent=7,separators=(": ","="),sort_keys=True)

print(carros_json)