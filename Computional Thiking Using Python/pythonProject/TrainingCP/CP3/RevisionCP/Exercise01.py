matriz = [[5,3,4,9,7,-5],[-8,-5,-6,-4,-4,-7],[-4,7,4,-8,2,-9]]

print("Desatualizada")
for i in range(3):
    print(matriz[i])

for i in range(3):
    for j in range(6):
        if(matriz[i][j] < 0):
            matriz[i][j] = 1

print("Atualizada")
for i in range(3):
    print(matriz[i])
