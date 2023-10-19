slr = []
nmrChild = []
slrMenor = 0

while True:
    vlrSlr = float(input("Salario (Digite um valor negativo p/ sair): "))
    if vlrSlr < 0:
        break
    slr.append(vlrSlr)
    if vlrSlr < 150:
        slrMenor += 1

    qntChild = int(input("Filhos: "))
    nmrChild.append(qntChild)

print(f"Média do salário da população: {sum(slr)/len(slr)}")
print(f"Média de filhos da população: {sum(nmrChild)/len(nmrChild)}")
print(f"Maior salário dos habitantes: {max(slr)}")
print(f"Percentual que recebe menos que 150 reais: {(slrMenor*100)/len(slr)}%")

