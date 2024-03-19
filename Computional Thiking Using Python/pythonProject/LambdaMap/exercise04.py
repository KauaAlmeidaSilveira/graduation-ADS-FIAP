listLetras = ['E', 'O', 'R', 'G','a', 'b', 'c', 'd']

listInverso = list(map(lambda letra: letra.lower() if letra.isupper() else letra.upper(), listLetras))

print(listInverso)
