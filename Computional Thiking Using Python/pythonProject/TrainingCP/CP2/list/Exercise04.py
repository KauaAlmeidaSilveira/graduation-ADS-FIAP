loop = 0
listValues = []
soma = 0


while(loop != -1):
    loop = int(input("num: "))
    if(loop != -1):
        listValues.append(loop)

for i in listValues:
    soma += i

vlrMaiorQueMedia = []
vlrMenorQueSete = []

print(f"Soma de todos os valores: {soma}")
print(f"Média: {soma/listValues.__len__()}")

for i in listValues:
    if(i > soma/listValues.__len__()):
        vlrMaiorQueMedia.append(i)
    if(i < 7):
        vlrMenorQueSete.append(i)

print(f"Valores maiores que a média: {vlrMaiorQueMedia}")
print(f"Valores menores que sete: {vlrMaiorQueMedia}")