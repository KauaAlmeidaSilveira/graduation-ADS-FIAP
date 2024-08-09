print("Vamos armazenar 5 clientes !!\n")

listClients = []

for i in range(2):
    cliente = {
        "Id": int(input("Digite o id do " + str(i + 1) + "º cliente: ")),
        "Nome": input("Digite o nome do " + str(i + 1) + "º cliente: "),
        "Logradouro": input("Digite o logradouro do " + str(i + 1) + "º cliente: "),
        "Bairro": input("Digite o bairro do " + str(i + 1) + "º cliente: "),
        "Cidade": input("Digite a cidade do " + str(i + 1) + "º cliente: "),
        "Idade": int(input("Digite a idade do " + str(i + 1) + "º cliente: ")),
        "limiteCredito": float(input("Digite o limite de crédito do " + str(i + 1) + "º cliente: "))
    }
    listClients.append(cliente)

for listClient in listClients:
    if listClient["Idade"] > 35 and listClient["Cidade"] == "São Paulo":
        print(listClient)

for listClient in listClients:
    if listClient["limiteCredito"] > 5000 and listClient["Cidade"] == "Rio de Janeiro":
        print(listClient)