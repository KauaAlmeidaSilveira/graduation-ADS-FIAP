# Ler do arquivo texto e armazenar em uma lista de dicionários
nome_arq = input("Digite um nome para o arquivo texto (com extensão): ")
with open(nome_arq,"r") as arq:
    lista_dados = arq.readlines()

lista_contatos = []

for dados in lista_dados:
    contato = dados.split("*")
    dic_contato = {
        'Codigo':int(contato[0]),
        'Nome':contato[1],
        'Telefone':contato[2]
    }
    lista_contatos.append(dic_contato)

print(lista_contatos)
