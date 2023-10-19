# Inicialize as listas vazias para números, pares e ímpares
numeros = []
pares = []
impares = []

# Leitura de 10 números inteiros
for i in range(10):
    numero = int(input(f'Digite o {i + 1}º número inteiro: '))
    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Imprima as 3 listas
print("Números digitados:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)
