import json

objs = [
    {"cod": 15, "nome": "diego", "idade": 12, "slr": 56453.0},

    {"cod": 45, "nome": "abel", "idade": 123, "slr": 45234.0},

    {"cod": 23, "nome": "huan", "idade": 21, "slr": 6543.0}
]

with open("teste.json", "r") as arq:
    listJson = arq.read()
    listaObjs = json.loads(listJson)

for i in listaObjs:
    objs.append(i)

print(objs)

with open("teste.json", "w") as arq:
    json.dump(objs, arq, indent='\t', ensure_ascii=False)

with open("teste.json", "r") as arq:
    listJson = arq.read()
    listaObjs = json.loads(listJson)

print(listaObjs)
