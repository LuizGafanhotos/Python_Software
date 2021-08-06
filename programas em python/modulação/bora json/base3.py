import json


jogador_j = '{"nome":"Luiz","time":"nenhum","vivo": "True","energia": 100,"mochila": ["pederneira","corda","linha","arame"],"areonave":[{"tipo":"transporte","habilidade":70},{"tipo":"defesa","habilidade":100},{"tipo":"reconhecimento","habilidade":20}]}'

jogador = json.loads(jogador_j)
print("As bolsas do jogador")
print("-"*29)
for im in jogador["mochila"]:
    print(im)

print("-"*29)
print("As aeronaves")
for a in jogador["areonave"]:
    print(a)