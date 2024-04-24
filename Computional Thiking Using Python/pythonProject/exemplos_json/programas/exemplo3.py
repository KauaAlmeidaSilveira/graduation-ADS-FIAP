import json

lista_funcionarios = []

for i in range(3):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    salario = float(input("Salário: "))
    funcionario = {'Nome':nome,'Idade':idade,'Salario':salario}
    lista_funcionarios.append(funcionario)

with open("funcionarios.json","w",encoding="utf-8") as arq:
    json.dump(lista_funcionarios,arq,indent = '\t',ensure_ascii=False)

with open("funcionarios.json","r",encoding="utf-8") as arq:
    arqJson = arq.read()
    lista = json.loads(arqJson)

print(lista)