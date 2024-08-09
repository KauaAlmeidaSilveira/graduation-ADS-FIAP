numList = [1,5,6,7,2,31,52,7,15,62,47]

listPar = list(map(lambda x: x if x%2 == 0 else 0, numList))

listImpar = list(map(lambda x: x if x%2 != 0 else 0, numList))

print(listPar)
print(listImpar)

resultPar = sum(listPar)
resultImpar = sum(listImpar)

print(f"Par: {resultPar} \nImpar: {resultImpar}")