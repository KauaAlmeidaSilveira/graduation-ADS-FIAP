matriz = [[1, 3, 4], [7, 8, 95], [1, 5, 12]]

sumMaiorLinha = 0
posicaoMaiorLinha = 0

for i, linha in enumerate(matriz):
    soma = sum(linha)
    if soma > sumMaiorLinha:
        sumMaiorLinha = soma
        posicaoMaiorLinha = i

print(matriz[posicaoMaiorLinha])
print(f"Soma: {sumMaiorLinha}")