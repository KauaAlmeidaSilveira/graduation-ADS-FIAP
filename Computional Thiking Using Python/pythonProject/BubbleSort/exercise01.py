list_func = []


def main():
    while True:

        resp = int(input("01 - Adicionar\n"
                         "02 - Listar\n"
                         "03 - Atualizar\n"
                         "04 - Remover\n\n"
                         "05 - SAIR\n\n"
                         "Digite a opção que deseja: "))

        match resp:
            case 1:
                adicionar()
            case 2:
                listar()
            case 3:
                atualizar()
            case 4:
                remover()
            case 5:
                break
            case _:
                print('Não entendi !!')


def adicionar():
    try:
        cod = int(input("cod: "))

        while True:
            if not exists(cod):
                break
            else:
                cod = int(input("Código já existente, por favor, insira outro código"))

        nome = input("nome: ")

        idade = int(input("idade: "))

        slr = float(input("slr: "))

    except ValueError:
        print("Digite dados válidos")

    else:
        list_func.append(
            {
                "cod": cod,
                "nome": nome,
                "idade": idade,
                "slr": slr
            }
        )
    finally:
        print("Fim da inserção")


def listar():
    for i in list_func:
        print(f"{i}\n")


def exists(cod):
    for i in list_func:
        if i["cod"] == cod:
            return True


def atualizar():
    cod = int(input("Digite o código do func: "))

    if exists(cod):
        for i in list_func:
            if i["cod"] == cod:
                i["nome"] = input("nome: ")
                i["idade"] = int(input("idade: "))
                i["slr"] = float(input("slr: "))
        print("Atualizado !!")
    else:
        print("Não encontrado !!")


def remover():
    cod = int(input("Digite o código do func: "))

    if exists(cod):
        for i, obj in enumerate(list_func):
            if obj["cod"] == cod:
                list_func.pop(i)
        print("Deletado !!")
    else:
        print("Não encontrado !!")


if __name__ == '__main__':
    main()
