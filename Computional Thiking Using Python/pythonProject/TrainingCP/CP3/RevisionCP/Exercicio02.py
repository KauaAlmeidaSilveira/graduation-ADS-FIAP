matriz = [[1,6,7,2,8],[2,3,4,9,7],[6,7,2,8,9],[4,6,98,2,4],[7,9,5,3,4]]

for i in range(5):
    diagonal_valor = matriz[i][i]  # Valor na diagonal principal
    for j in range(5):
        matriz[i][j] *= diagonal_valor

for i in range(5):
    print(matriz[i])