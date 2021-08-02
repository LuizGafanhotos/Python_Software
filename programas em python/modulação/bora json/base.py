import json

carros_json = '{"marca": "honda","modelo": "HRV","cor": "prata"}'

carros = json.loads(carros_json)

for x,y in carros.items():
    print(x + " - " +  y)

print("-="*28)

motos = '{"marca": "honda","modelo": "HRV","cor": "prata"}'
motos_json = json.dumps(motos)

print(motos_json)