ingles = []
portugues = []

while True:
    palavra_ingles = input("Digite uma palavra em inglês (ou 0 para sair): ")

    if palavra_ingles == '0':
        break

    traducao_portugues = input(f"Digite a tradução em português de '{palavra_ingles}': ")

    ingles.append(palavra_ingles)
    portugues.append(traducao_portugues)

while True:
    palavra_busca = input("Digite uma palavra em inglês para encontrar a tradução (ou 0 para sair): ")

    if palavra_busca == '0':
        break

    if palavra_busca in ingles:
        indice = ingles.index(palavra_busca)
        traducao = portugues[indice]
        print(f"A tradução de '{palavra_busca}' em português é '{traducao}'.")
    else:
        print(f"A palavra '{palavra_busca}' não está no dicionário.")
