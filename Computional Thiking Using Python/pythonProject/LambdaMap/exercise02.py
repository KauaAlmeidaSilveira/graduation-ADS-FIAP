listaOriginal = [234, 64, 13467, 45.89, 23]
listaDescontos = [0.3, 0.004, 0.5, 0.03, 0.8]


listResult = list(map(lambda x, y: x - (x*y), listaOriginal, listaDescontos))


print(listResult)
