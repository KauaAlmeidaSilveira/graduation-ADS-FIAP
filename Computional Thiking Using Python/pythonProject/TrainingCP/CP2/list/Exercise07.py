numeros = []
multiplosDeTres = 0

for i in range(10):
    numero = int(input(f'Digite o {i + 1}º número inteiro: '))
    numeros.append(numero)
    if numero % 3 == 0:
        multiplosDeTres += 1

print(multiplosDeTres)