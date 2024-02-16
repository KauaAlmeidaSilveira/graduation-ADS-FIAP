# EXERCISE 01

list = [1, 2, 3, 5]


def ler_lista(list, size):
    for i in range(size):
        print(list[i])


def media_impares(list, size):
    sum = 0
    for i in range(size):
        if list[i] % 2 != 0:
            sum += list[i]
    print(sum / size)


def busca_numero(num, list, size):
    for i in range(size):
        if list[i] == num:
            return i
    return -1


print("== A ==")
ler_lista(list, 4)

print("\n== B ==")
media_impares(list, 4)

print("\n== C ==")
index = busca_numero(3, list, 4)
print(index)