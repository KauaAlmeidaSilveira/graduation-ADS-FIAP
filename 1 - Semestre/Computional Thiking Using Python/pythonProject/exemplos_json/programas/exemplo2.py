import json

with open("alunos_idade.json","r",encoding="utf-8") as arq:
    arqJson = arq.read()
    lista = json.loads(arqJson)

print(lista)