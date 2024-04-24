import json

with open("log.json","r",encoding="utf-8") as arq:
    arqJson = arq.read()
    lista = json.loads(arqJson)

print(lista)

print(f"TimeStamp: {lista[0]['timeStamp']}")
print(f"tableName: {lista[0]['tableName']}")