list_alunos = []


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
        cod = int(input("Digite o código do aluno: "))
        while True:
            if not exists(cod):
                break
            else:
                print("Código já existente, por favor, insira outro código")
                cod = int(input("Digite o código do aluno: "))
        nome = input("Digite o nome do aluno: ")
        curso = input("Digite o curso do aluno: ")
        disciplina = input("Digite a disciplina do aluno: ")
        faltas = int(input("Digite as faltas do aluno: "))
        lista_cps = []
        for i in range(3):
            lista_cps.append(float(input(f"Digite a nota do {1+i}º CP: ")))

    except ValueError:
        print("Digite dados válidos")
    else:
        list_alunos.append(
            {
                "cod": cod,
                "nome": nome,
                "curso": curso,
                "disciplina": disciplina,
                "faltas": faltas,
                "cps": lista_cps
            }
        )
        print("aluno inserido com sucesso!")
    finally:
        print("Fim da inserção")


def deleteById():
    cod = int(input("Digite o código do aluno que deseja remover: "))
    for i in list_alunos:
        if i["cod"] == cod:
            list_alunos.remove(i)
    print("aluno removido com sucesso!")


def findAll():
    for i in list_alunos:
        print(i)


def exists(cod):
    for i in list_alunos:
        if i["cod"] == cod:
            return True
    return False


def update():
    try:
        cod = int(input("Digite o código do aluno que deseja atualizar: "))
        while True:
            if exists(cod):
                nome = input("Digite o nome do aluno: ")
                curso = input("Digite a curso do aluno: ")
                disciplina = input("Digite o disciplina do aluno: ")
                faltas = int(input("Digite as faltas do aluno: "))
                lista_cps = []
                resp = input("Deseja atualizar as notas dos CPs (S-SIM/N-NÃO)? ")
                if resp.upper() == "S":
                    for i in range(3):
                        lista_cps.append(float(input(f"Digite a nota do {1+i}º CP: "))
                    )
                break
            else:
                print("Código não existente, por favor, insira outro código")
                cod = int(input("Digite o código do aluno: "))
    except ValueError:
        print("Digite dados válidos")
    else:
        for i in list_alunos:
            if i["cod"] == cod:
                if bool(nome):
                    i["nome"] = nome
                if bool(curso):
                    i["curso"] = curso
                if bool(disciplina):
                    i["disciplina"] = disciplina
                if bool(faltas):
                    i["faltas"] = faltas
                if bool(lista_cps):
                    i["cps"] = lista_cps
        print("aluno atualizado com sucesso!")
    finally:
        print("Fim da atualização")


if __name__ == '__main__':
    main()
