# Abertura do arquivo para escrita - Modo de abertura "append"

lista_contatos = []

for i in range (3):
    codigo = int(input("Digite o código do contato: "))
    nome = input("digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    contato = {'Codigo':codigo,'Nome':nome,'Telefone':telefone}
    lista_contatos.append(contato)

# Percorrer a lista para gravar os dados em um arquivo texto
nome_arq = input("Digite um nome para o arquivo texto (com extensão): ")
for i in range (3):
    linha = str(lista_contatos[i]['Codigo'])+"*"+lista_contatos[i]['Nome']+"*"+lista_contatos[i]['Telefone']+"\n"
    with open(nome_arq,"a") as arq:
        arq.write(linha)
