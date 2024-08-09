if __name__ == '__main__':
    notas = []

    qnt_notas = int(input("Quantas notas deseja adicionar ? "))

    def armazenar_notas(lista, size):
        for i in range(size):
            lista.append(float(input(f"Digite a nota {i + 1}º: ")))

    armazenar_notas(notas, qnt_notas)

    print("\nNOTAS: ")
    for nota in notas:
        print(nota)

    def media_notas(lista):
        _sum = 0.0

        for nota in lista:
            _sum += nota

        return round(_sum / len(lista), 2)

    print(f"\nMÉDIA: {media_notas(notas)}")

    def notas_acima_de_sete(lista):
        _new_list = []

        for nota in lista:
            if nota > 7:
                _new_list.append(nota)

        return _new_list

    print("\nNOTAS ACIMA DE SETE: ")
    for notas in notas_acima_de_sete(notas):
        print(notas)