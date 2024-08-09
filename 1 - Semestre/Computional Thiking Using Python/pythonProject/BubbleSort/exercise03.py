nomes = [
    "kaua",
    "bia",
    "caio",
    "enaldo",
    "mario",
    "pedro",
    "thiago",
    "naryeli"
]

print(nomes)


def bubbleSort(array):
    for j in array:
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]


bubbleSort(nomes)

print(nomes)


def buscaBin(array, item, ini=0, fim=None):
    if fim is None:
        fim = len(array) - 1

    if ini <= fim:
        m = (ini + fim) // 2
        if array[m] == item:
            return m
        if item < array[m]:
            return buscaBin(array, item, ini, m - 1)
        else:
            return buscaBin(array, item, m + 1, fim)


print(buscaBin(nomes, "thiago"))

import json

with open("teste.json", "r") as arq:
    arq_json = arq.read()
    lista = json.loads(arq_json)





