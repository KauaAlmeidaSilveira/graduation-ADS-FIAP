def main():
    lista = []
    tam = int(input("Digite o tamanho da lista: "))

    ler_lista(lista, tam)
    print(lista)
    bubbleSort(lista)
    print(lista)

def ler_lista(lista,tam):
    for i in range(tam):
        lista.append(int(input("Digite um elemento da lista: ")))

def bubbleSort (lista):

    tam = len(lista)
    for i in range(tam-1,0,-1):
        for j in range(i):

            if lista[j] > lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp

if __name__ == "__main__":
    main()