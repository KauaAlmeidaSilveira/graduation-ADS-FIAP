array = [
    {
        "nome": "kaua",
        "idade": 18
    },
    {
        "nome": "naryeli",
        "idade": 25
    }
]

for i in array:
    linha = i["nome"] + ";" + str(i["idade"]) + "\n"
    with open("func.txt", "a") as arq:
        arq.write(linha)
