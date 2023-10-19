vlrs = []
dentroDoIntervalo = 0

for i in range(10):
    vlrNum = int(input(f'Digite o {i + 1}º número inteiro: '))
    vlrs.append(vlrNum)

    if 10 <= vlrNum <= 20:
        dentroDoIntervalo += 1

print(f"Qnt de numeros dentro do intervalo: {dentroDoIntervalo} e fora {len(vlrs)-dentroDoIntervalo}")


