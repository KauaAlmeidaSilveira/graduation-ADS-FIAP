list_clientes = []


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
        cod = int(input("Digite o código do cliente: "))
        while True:
            if not exists(cod):
                break
            else:
                print("Código já existente, por favor, insira outro código")
                cod = int(input("Digite o código do cliente: "))
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite a cpf do cliente: ")
        idade = int(input("Digite o idade do cliente: "))
        endereco = input("Digite as endereco do cliente: ")
        limite_credito = float(input("Digite o limite de crédito do cliente: "))

    except ValueError:
        print("Digite dados válidos")
    else:
        list_clientes.append(
            {
                "cod": cod,
                "nome": nome,
                "cpf": cpf,
                "idade": idade,
                "endereco": endereco,
                "limite_credito": limite_credito
            }
        )
        print("cliente inserido com sucesso!")
    finally:
        print("Fim da inserção")


def deleteById():
    cod = int(input("Digite o código do cliente que deseja remover: "))
    for i in list_clientes:
        if i["cod"] == cod:
            list_clientes.remove(i)
    print("cliente removido com sucesso!")


def findAll():
    for i in list_clientes:
        print(i)


def exists(cod):
    for i in list_clientes:
        if i["cod"] == cod:
            return True
    return False


def update():
    try:
        cod = int(input("Digite o código do cliente que deseja atualizar: "))
        while True:
            if exists(cod):
                nome = input("Digite o nome do cliente: ")
                cpf = input("Digite a cpf do cliente: ")
                idade = int(input("Digite o idade do cliente: "))
                endereco = input("Digite as endereco do cliente: ")
                limite_credito = float(input("Digite o limite de crédito do cliente: "))
                break
            else:
                print("Código não existente, por favor, insira outro código")
                cod = int(input("Digite o código do cliente: "))
    except ValueError:
        print("Digite dados válidos")
    else:
        for i in list_clientes:
            if i["cod"] == cod:
                if bool(nome):
                    i["nome"] = nome
                if bool(cpf):
                    i["cpf"] = cpf
                if bool(idade):
                    i["idade"] = idade
                if bool(endereco):
                    i["endereco"] = endereco
                if bool(limite_credito):
                    i["limite_credito"] = limite_credito
        print("cliente atualizado com sucesso!")
    finally:
        print("Fim da atualização")


if __name__ == '__main__':
    main()
