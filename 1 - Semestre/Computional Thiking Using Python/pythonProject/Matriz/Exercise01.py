matriz = [[1,3,4,5],[7,8,95,78],[1,5,12,6],[17,10,1,2]]
nmrMaiores = 0

for i in range(4):
    for j in range(4):
        if(matriz[i][j] > 10):
            nmrMaiores += 1

print(nmrMaiores)




