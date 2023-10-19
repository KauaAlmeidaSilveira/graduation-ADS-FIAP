idades = []
menoresDeIdade = 0

while True:
    idade = int(input("Idade (-1 para encerrar): "))

    if idade == -1:
        break

    idades.append(idade)

    if idade < 18:
        menoresDeIdade += 1

print(f"Menores de idade: {menoresDeIdade}")
print(f"Média das idades: {(sum(idades)/len(idades)).__round__(2)}")

