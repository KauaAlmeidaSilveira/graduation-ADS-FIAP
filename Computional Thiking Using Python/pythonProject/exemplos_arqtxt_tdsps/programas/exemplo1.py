# Leitura do arquivo texto - Dados do arquivo como string
'''
with open("contatos.txt", "r", encoding="utf-8") as arq:
    dados = arq.read()

print(dados)
print(type(dados))
'''
# Leitura do arquivo texto - Dados do arquivo como listas

with open("contatos.txt", "r", encoding="utf-8") as arq:
    lista_dados = arq.readlines()

print(lista_dados)

for dados in lista_dados:
    print(dados.split())
