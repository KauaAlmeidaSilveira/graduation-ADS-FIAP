list_products = []


def main():
    while True:
        print("1 - Inserir")
        print("2 - Remover")
        print("3 - Listar")
        print("4 - Atualizar")
        print("5 - Sair")
        resp = int(input("Digite a opção desejada: "))
        match resp:
            case 1:
                insert()
            case 2:
                deleteById()
            case 3:
                findAll()
            case 4:
                update()
            case 5:
                print("Saindo...Até mais!")
                break
            case _:
                print("Opção inválida")
        resp = input("Deseja continuar (S-SIM/N-NÃO)? ")
        if resp.upper() == "N":
            print("Saindo...Até mais!")
            break


def insert():
    try:
        cod = int(input("Digite o código do produto: "))
        while True:
            if not exists(cod):
                break
            else:
                print("Código já existente, por favor, insira outro código")
                cod = int(input("Digite o código do produto: "))
        desc = input("Digite o desc do produto: ")
        qnt = int(input("Digite a qnt do produto: "))
        vlr = float(input("Digite o vlr do produto: "))

    except ValueError:
        print("Digite dados válidos")
    else:
        list_products.append(
            {
                "cod": cod,
                "desc": desc,
                "qnt": qnt,
                "vlr": vlr
            }
        )
        print("produto inserido com sucesso!")
    finally:
        print("Fim da inserção")


def deleteById():
    cod = int(input("Digite o código do produto que deseja remover: "))
    for i in list_products:
        if i["cod"] == cod:
            list_products.remove(i)
    print("produto removido com sucesso!")


def findAll():
    for i in list_products:
        print(i)


def exists(cod):
    for i in list_products:
        if i["cod"] == cod:
            return True
    return False


def update():
    try:
        cod = int(input("Digite o código do produto que deseja atualizar: "))
        while True:
            if exists(cod):
                desc = input("Digite o desc do produto: ")
                qnt = int(input("Digite a qnt do produto: "))
                vlr = float(input("Digite o vlr do produto: "))
                break
            else:
                print("Código não existente, por favor, insira outro código")
                cod = int(input("Digite o código do produto: "))
    except ValueError:
        print("Digite dados válidos")
    else:
        for i in list_products:
            if i["cod"] == cod:
                if bool(desc):
                    i["desc"] = desc
                if bool(qnt):
                    i["qnt"] = qnt
                if bool(vlr):
                    i["vlr"] = vlr
        print("produto atualizado com sucesso!")
    finally:
        print("Fim da atualização")


if __name__ == '__main__':
    main()
