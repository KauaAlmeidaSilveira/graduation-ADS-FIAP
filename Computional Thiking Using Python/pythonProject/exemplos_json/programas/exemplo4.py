'''
Escreva um programa em Python que faça um CRUD em uma lista de dicionários, os quais devem conter
os seguintes dados:

Código

Nome do funcionário

Idade do funcionário

Salário do funcionário

Faça o tratamento de erros no processo de inserção e alteração. As operações deverão ser
executadas até que o usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO).
'''
import json
def main():
    tab_funcionario = []
    resp = 1

    while (resp != 0):
        print("1-Inserir funcionário")
        print("2-Alterar funcionário")
        print("3-Excluir funcionário")
        print("4-Exibir funcionários")
        print("5-Ordenar pelo nome")
        print("6-Buscar o funcionário pelo nome")
        print("7-Gravar os dados em um arquivo texto")
        print("8-Recuperar dados de um arquivo texto")
        print("9-Gravar os dados em um arquivo json")
        print("10-Recuperar dados de um arquivo json")
        opc = int(input("Digite a opção desejada (1-10): "))

        if (opc == 1):
                inserir_funcionario(tab_funcionario)
        elif (opc == 2):
                codigo = int(input("Digite o código do funcionário a ser alterado: "))
                indice = buscar_funcionario(tab_funcionario,codigo)
                if (indice != -1):
                    alterar_funcionario(tab_funcionario, indice)
                else:
                    print("Funcionário não encontrado")
        elif (opc == 3):
                codigo = int(input("Digite o código do funcionário a ser excluído: "))
                indice = buscar_funcionario(tab_funcionario, codigo)
                if (indice != -1):
                    excluir_funcionario(tab_funcionario, indice)
                else:
                    print("Funcionário não encontrado")
        elif (opc == 4):
                exibir_funcionarios(tab_funcionario)
        elif (opc == 5):
                ordenar_funcionarios(tab_funcionario)
                print("Tabela ordenada com sucesso! ")
        elif (opc == 6):
                ordenar_funcionarios (tab_funcionario)
                nome = input("Digite o nome a ser procurado: ")
                indice = buscaBin(tab_funcionario,nome)
                if (indice != -1):
                    print("O funcionário está cadastrado. Seus dados são os seguintes: ")
                    for chave,valor in tab_funcionario[indice].items():
                        print(f"{chave}: {valor}")
                else:
                    print("O funcionário não está cadastrado!")
        elif (opc == 7):
                criar_arqtxt(tab_funcionario)
        elif (opc == 8):
                recuperar_dados_arqtxt(tab_funcionario)
        elif (opc == 9):
                criar_json(tab_funcionario)
        elif (opc == 10):
                recuperar_dados_json(tab_funcionario)
        else:
                print("Opção inválida!")

        resp = int(input("Deseja continuar (1-SIM/0-NÃO)? "))

def criar_arqtxt(tab_funcionario):
    if (len(tab_funcionario) >= 1):
        nome_arq = input("Digite o nome do arquivo texto (com extensão): ")
        for i in range(len(tab_funcionario)):
            linha = str(tab_funcionario[i]['Codigo'])+"*"+tab_funcionario[i]['Nome']+"*"+str(tab_funcionario[i]['Idade'])+"*"+str(tab_funcionario[i]['Salario'])+"\n"
            with open(nome_arq,"a") as arq:
                arq.write(linha)
        print("Arquivo gravado com sucesso!")
    else:
        print("A tabela está vazia!")


def criar_json(tab_funcionario):
    if (len(tab_funcionario) >= 1):
        nome_arq = input("Digite o nome do arquivo json (com extensão): ")
        with open(nome_arq, "w", encoding="utf-8") as arq:
            json.dump(tab_funcionario, arq, ensure_ascii=False)
        print("Arquivo gravado com sucesso!")
    else:
        print("A tabela está vazia!")
def recuperar_dados_json(tab_funcionario):
    tab_funcionario.clear()
    nome_arq = input("Digite o nome do arquivo json (com extensão): ")
    with open(nome_arq, "r", encoding="utf-8") as arq:
        arqJson = arq.read()
        lista = json.loads(arqJson)
    for func in lista:
        tab_funcionario.append(func)
    print("Dados recuperados com sucesso!")

def ordenar_funcionarios (tab_funcionario):
    tam= len(tab_funcionario)
    for i in range(tam-1,0,-1):
        for j in range(i):
            if tab_funcionario[j]['Nome'] > tab_funcionario[j+1]['Nome']:
                temp = tab_funcionario[j]
                tab_funcionario[j] = tab_funcionario[j+1]
                tab_funcionario[j+1] = temp


def buscar_funcionario(tab_funcionario,codigo):
    indice = -1
    for i in range(len(tab_funcionario)):
        if (tab_funcionario[i]['Codigo'] == codigo):
            indice = i
    return(indice)


def buscaBin(tab_funcionario,nome):
    ini= 0
    fim = len(tab_funcionario) -1
    while(ini<= fim):
        meio = int((ini+fim)/2)
        if(tab_funcionario[meio]['Nome'] == nome):
            return(meio)
        else:
            if(nome< tab_funcionario[meio]['Nome']):
                fim = meio -1
            else:
                ini= meio + 1
    return(-1)

def inserir_funcionario(tab_funcionario):
    try:
        continua = 1
        while (continua != 0):
            codigo = int(input("Digite o código do funcionário: "))
            indice = buscar_funcionario(tab_funcionario,codigo)
            if (indice == -1):
                continua = 0
            else:
                continua = 1
                print("Código já existente!")

        nome = input("Digite o nome do funcionário: ")
        idade = int(input("Digite a idade do funcionário: "))
        salario = float(input("Digite o salário do funcionário: "))
    except ValueError:
        print("Digite dados numéricos! ")
    else:
        funcionario = {'Codigo': codigo, 'Nome': nome, 'Idade': idade, 'Salario': salario}
        tab_funcionario.append(funcionario)
    finally:
        print("Operação finalizada")

def alterar_funcionario(tab_funcionario,indice):
    try:
        print(f"Nome: {tab_funcionario[indice]['Nome']}")
        nome = input("Digite o novo nome: ")
        print(f"Idade: {tab_funcionario[indice]['Idade']}")
        idade = int(input("Digite o nova idade: "))
        print(f"Salário: {tab_funcionario[indice]['Salario']:.2f}")
        salario = float(input("Digite o novo salário: "))
    except ValueError:
        print("Digite dados numéricos")
    else:
        tab_funcionario[indice]['Nome'] = nome
        tab_funcionario[indice]['Idade'] = idade
        tab_funcionario[indice]['Salario'] = salario
        print("Funcionário alterado com sucesso! ")
    finally:
        print("Operação finalizada!")
    
def excluir_funcionario(tab_funcionario,indice):
    tab_funcionario.pop(indice)

    print("Funcionário excluído com sucesso! ")

def exibir_funcionarios(tab_funcionario):
    for i in range(len(tab_funcionario)):
        print(f"FUNCIONARIO {i+1}")
        for chave,valor in tab_funcionario[i].items():
            print(f"{chave}: {valor}")
        print("----------------------------------------")

if __name__ == "__main__":
    main()
