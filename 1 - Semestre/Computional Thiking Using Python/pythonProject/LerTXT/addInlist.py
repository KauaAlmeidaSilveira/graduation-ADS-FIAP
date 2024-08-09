array = []

with open("func.txt", "r") as arq:
    for func in arq.readlines():
        linha = func.split(";")
        array.append(
            {
                "nome": linha[0],
                "idade": int(linha[1])
            }
        )

for i in array:
    print(i)