listAllnotes = []
listNotasMaioresSete = []

for i in range(10):
    n1 = float(input("n1: "))
    n2 = float(input("n2: "))
    n3 = float(input("n3: "))
    media = (n1+n2+n3)/3
    listAllnotes.append(media.__round__(2))
    if media>7:
        listNotasMaioresSete.append(media.__round__(2))

print(f"Todas as notas: {listAllnotes}")
print(f"Notas maiores que sete: {listNotasMaioresSete}")

