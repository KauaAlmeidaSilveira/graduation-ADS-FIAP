list_func = [
    {'cod': 1, 'nome': 'kaua', 'idade': 12, 'slr': 56453.0},

    {'cod': 3, 'nome': 'kawa', 'idade': 123, 'slr': 45234.0},

    {'cod': 2, 'nome': 'kawan', 'idade': 21, 'slr': 6543.0}
]


def main():
    while True:

        resp = int(input("01 - Adicionar\n"
                         "02 - Listar\n"
                         "03 - Listar ordenado pelo nome\n"
                         "04 - Atualizar\n"
                         "05 - Remover\n"
                         "06 - Buscar index pelo nome\n\n"

                         "07 - SAIR\n\n"
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
                nome = input("Digite o nome: ")
                print(f"Posição: {buscaBinaria(list_func, nome)}")
            case 7:
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
    n = len(list)
    for j in range(n - 1):
        for i in range(n - 1):
            if list[i]["nome"] > list[i + 1]["nome"]:
                list[i], list[i + 1] = list[i + 1], list[i]
    return list


def buscaBinaria(array, item, ini=0, fim=None):
    if fim is None:
        fim = len(array) - 1

    if ini <= fim:
        m = (ini + fim) // 2
        if array[m]["nome"] == item:
            return m
        if item < array[m]["nome"]:
            return buscaBinaria(array, item, ini, m - 1)
        else:
            return buscaBinaria(array, item, m + 1, fim)
    return None


if __name__ == '__main__':
    main()
