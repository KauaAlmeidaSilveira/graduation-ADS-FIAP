'''
Escreva um programa em Python que faça um CRUD em uma lista de dicionários, os quais devem conter os seguintes dados: 

Código 

Nome do funcionário 

Idade do funcionário 

Salário do funcionário 

Faça o tratamento de erros no processo de inserção e alteração. As operações deverão ser executadas até que o usuário digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO). 
'''


def main():
    resp = "S"
    lista_funcionarios = []

    while(resp != "N"):
        print("1 - Inserir funcionario")
        print("2 - Alterar funcionario")
        print("3 - Excluir funcionario")
        print("4 - Exibir funcionarios")
        print("5 - Ordenação (bubble sort) pelo nome")
        opc = int(input("Digite a opção desejada (1-5): "))
        match opc:
            case 1:
                inserir_funcionario(lista_funcionarios)
            case 2:
                codigo = int(input("Digite o código do funcionário a ser alterado: "))
                indice = buscar_funcionario(lista_funcionarios,codigo)
                if (indice != -1):
                    alterar_funcionario(lista_funcionarios, indice)
                else:
                    print("Código do funcionario não encontrado!")
            case 3:
                codigo = int(input("Digite o código do funcionário a ser excluído: "))
                indice = buscar_funcionario(lista_funcionarios, codigo)
                if (indice != -1):
                    excluir_funcionario(lista_funcionarios, indice)
                else:
                    print("Código do funcionario não encontrado!")
            case 4:
                exibir_funcionarios(lista_funcionarios)
            case 5:
                bubbleSort(lista_funcionarios,'Nome')
            case _:
                print("Opção inválida!")
        resp = input("Deseja continuar (S-SIM/N-NÃO)? ")

def buscar_funcionario(lista_funcionarios,codigo):
    indice = -1
    for i in range(len(lista_funcionarios)):
        if (lista_funcionarios[i]['Codigo'] == codigo):
            indice = i
    return(indice)

def inserir_funcionario(lista_funcionarios):
    try:
        continua = 1
        while (continua != 0):
            codigo = int(input("Digite o código do funcionário: "))
            indice = buscar_funcionario(lista_funcionarios,codigo)
            if (indice!=-1): # já existe o código que o usuário quer cadastrar
                print("O código já existe na tabela! ")
            else:
                continua = 0
        nome = input("Digite o nome do funcionario: ")
        idade = int(input("Digite a idade do funcionario: "))
        salario = float(input("Digite o salário do funcionario: "))
    except ValueError:
        print("Digite dados numéricos!")
    else:
        funcionario = {'Codigo': codigo, 'Nome': nome, 'Idade': idade, 'Salario': salario}
        lista_funcionarios.append(funcionario)
        print("Dados cadastrados com sucesso!")
    finally:
        print("Operação finalizada! ")



def alterar_funcionario(lista_funcionarios,indice):
    try:
        print(f"Nome do funcionario: {lista_funcionarios[indice]['Nome']}")
        nome = input("Digite o novo nome do funcionário: ")
        print(f"Idade do funcionario: {lista_funcionarios[indice]['Idade']}")
        idade = int(input("Digite a idade do funcionário: "))
        print(f"Salário do funcionario: {lista_funcionarios[indice]['Salario']}")
        salario = float(input("Digite o novo salário do funcionário: "))
    except ValueError:
        print("Digite valores numéricos! ")
    else:
        lista_funcionarios[indice]['Nome'] = nome
        lista_funcionarios[indice]['Idade'] = idade
        lista_funcionarios[indice]['Salario'] = salario
        print("Funcionario alterado com sucesso!!")
    finally:
        print("Operação finalizada")

def excluir_funcionario(lista_funcionarios,indice):
    lista_funcionarios.pop(indice)
    print("Funcionário excluído com sucesso")

def exibir_funcionarios(lista_funcionarios):
    for i in range(len(lista_funcionarios)):
        print(f"FUNCIONÁRIO {i+1}")
        for chave,valor in lista_funcionarios[i].items():
            print(f"{chave}: {valor}")
        print("----------------------------------------------")

def bubbleSort (lista_funcionarios,chave):

    tam = len(lista_funcionarios)
    for i in range(tam-1,0,-1):
        for j in range(i):

            if lista_funcionarios[j][chave] > lista_funcionarios[j+1][chave]:
                temp = lista_funcionarios[j]
                lista_funcionarios[j] = lista_funcionarios[j+1]
                lista_funcionarios[j+1] = temp

if __name__ == "__main__":
    main()
