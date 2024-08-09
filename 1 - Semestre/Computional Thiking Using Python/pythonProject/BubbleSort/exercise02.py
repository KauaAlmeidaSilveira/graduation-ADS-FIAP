array = [2, 1, 5, 4, 3]


def bubbleSort(array):
    n = len(array)

    for j in range(n - 1):
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]


print(array)

bubbleSort(array)

print(array)


def buscaBinaria(array, item, ini=0, fim=None):

    if fim is None:
        fim = len(array)

    m = (ini + fim) // 2

    if array[m] == item:
        return m
    if item < array[m]:
        return buscaBinaria(array, item, ini, m - 1)
    else:
        return buscaBinaria(array, item, m + 1, fim)


print(buscaBinaria(array, 4))