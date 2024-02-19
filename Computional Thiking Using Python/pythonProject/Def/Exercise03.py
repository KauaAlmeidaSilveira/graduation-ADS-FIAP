if __name__ == '__main__':
    palavras = []

    def carregar_palavras(lista):
        for i in range(10):
            lista.append(input(f"{i + 1}º - palavra: "))

    carregar_palavras(palavras)

    def eh_palindromo(lista):
        palindromo = 0

        for palavra in lista:
            palavra = palavra.lower()
            if palavra == ''.join(reversed(palavra)):
                palindromo += 1

        return palindromo


    print(f"Nessas palavras, apenas {eh_palindromo(palavras)} são palindromos !!")