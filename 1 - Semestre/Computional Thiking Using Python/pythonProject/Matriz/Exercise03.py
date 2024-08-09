matriz = [[1,754,4],[7,981,95],[1,5,12],[1,112,4],[7,8,95],[1,713,12]]
maiorNumero = matriz[0][0]
posicaoMaior = 0
menorNumero = matriz[0][0]
posicaoMenor = 0

for i in range(6):
    for j in range(3):
        if(maiorNumero < matriz[i][j]):
            maiorNumero = matriz[i][j]
            posicaoMaior = (i, j)
        if(menorNumero > matriz[i][j]):
            menorNumero = matriz[i][j]
            posicaoMenor = (i, j)

print(f"Maior numero: {maiorNumero}, posição {posicaoMaior}")
print(f"Menor numero: {menorNumero}, posição {posicaoMenor}")
