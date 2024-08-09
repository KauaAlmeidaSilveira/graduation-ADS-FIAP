matriz = [[1,3,4],[7,8,95],[1,5,12]]
k = 2

for i in range(3):
    for j in range(3):
        if(i == j):
            print(matriz[i][j])

print("Com valores multiplicados:")

for i in range(3):
    for j in range(3):
        if(i == j):
            print(matriz[i][j]*k)