numeros = []

for i in range(10):
    numero = int(input(f'Digite o {i + 1}º número inteiro: '))
    numeros.append(numero)

num = max(numeros)

print(f"O maior nmr é: {num}, posição {numeros.index(num)}")