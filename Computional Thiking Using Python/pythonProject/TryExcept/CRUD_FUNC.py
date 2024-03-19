list_func = []


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
        cod = int(input("Digite o código do funcionário: "))
        while True:
            if not exists(cod):
                break
            else:
                print("Código já existente, por favor, insira outro código")
                cod = int(input("Digite o código do funcionário: "))
        nome = input("Digite o nome do funcionário: ")
        idade = int(input("Digite a idade do funcionário: "))
        salario = float(input("Digite o salário do funcionário: "))

    except ValueError:
        print("Digite dados válidos")
    else:
        list_func.append(
            {
                "cod": cod,
                "nome": nome,
                "idade": idade,
                "salario": salario
            }
        )
        print("Funcionário inserido com sucesso!")
    finally:
        print("Fim da inserção")


def deleteById():
    cod = int(input("Digite o código do funcionário que deseja remover: "))
    for i in list_func:
        if i["cod"] == cod:
            list_func.remove(i)
    print("Funcionário removido com sucesso!")


def findAll():
    for i in list_func:
        print(i)


def exists(cod):
    for i in list_func:
        if i["cod"] == cod:
            return True
    return False


def update():
    try:
        cod = int(input("Digite o código do funcionário que deseja atualizar: "))
        while True:
            if exists(cod):
                nome = input("Digite o nome do funcionário: ")
                idade = int(input("Digite a idade do funcionário: "))
                salario = float(input("Digite o salário do funcionário: "))
                break
            else:
                print("Código não existente, por favor, insira outro código")
                cod = int(input("Digite o código do funcionário: "))
    except ValueError:
        print("Digite dados válidos")
    else:
        for i in list_func:
            if i["cod"] == cod:
                if bool(nome):
                    i["nome"] = nome
                if bool(idade):
                    i["idade"] = idade
                if bool(salario):
                    i["salario"] = salario
        print("Funcionário atualizado com sucesso!")
    finally:
        print("Fim da atualização")


if __name__ == '__main__':
    main()
