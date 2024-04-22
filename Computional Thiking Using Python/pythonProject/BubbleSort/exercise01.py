list_func = []


def main():
    while True:

        resp = int(input("01 - Adicionar\n"
                         "02 - Listar\n"
                         "03 - Listar ordenado pelo nome\n"
                         "04 - Atualizar\n"
                         "05 - Remover\n\n"
                         "06 - SAIR\n\n"
                         "Digite a opção que deseja: "))

        match resp:
            case 1:
                adicionar()
            case 2:
                listar(list_func)
            case 3:
                listar(bubble_sort(list_func))
            case 4:
                atualizar()
            case 5:
                remover()
            case 6:
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
                cod = int(input("Código já existente, por favor, insira outro código: "))

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


def listar(list):
    for i in list:
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


def bubble_sort(list):

    copyList = []
    for i in list:
        copyList.append(i)

    n = len(copyList)
    for j in range(n - 1):
        for i in range(n - 1):
            if copyList[i]["nome"] > copyList[i + 1]["nome"]:
                copyList[i], copyList[i + 1] = copyList[i + 1], copyList[i]
    return copyList


if __name__ == '__main__':
    main()
