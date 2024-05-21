import oracledb
import pandas as pd


def main():
    conexao, inst_SQL, conn = conecta_BD()

    opc = 0

    while opc != 9 and conexao:
        print("1-Cadastro de Medicamento")
        print("2-Cadastro de Laboratorio")
        print("3-Relatório de todos os Medicamentos por laboratório")
        print("4-Relatório de todos Medicamentos do laboratório esquilhido cujo valor seja maior do que 70,00")
        print("5-Relatório de todos Medicamentos do laboratório esquilhido cujo valor esteja entre 100,00 e 250,00")
        print("6-Exportar relatório de todos os Medicamentos por laboratório para um arquivo TXT")
        print("7-Exportar relatório de todos os Medicamentos\n"
              "  do laboratório esquilhido cujo valor seja maior do que 70,00 para um arquivo TXT")
        print("8-Exportar relatório de todos os Medicamentos\n"
              "  do laboratório esquilhido cujo valor esteja entre 100,00 e 250,00 para um arquivo TXT")
        print("9-Sair")

        try:
            opc = int(input("Digite a opcao (1-9): "))
        except ValueError:
            print("Por favor, digite um número válido.")

        # Cadastro de Medicamentos
        if opc == 1:
            resp = 0

            while resp != 5:
                print("1-Inserção")
                print("2-Alteração")
                print("3-Exclusão")
                print("4-Listar todos")
                print("5-Voltar")
                try:
                    resp = int(input("Digite a opcao (1-5): "))
                except ValueError:
                    print("Por favor, digite um número válido.")

                if resp == 1:
                    insertMedicamento(inst_SQL, conn)
                elif resp == 2:
                    buscarMedicamentos(inst_SQL)
                    updateMedicamento(inst_SQL, conn)
                elif resp == 3:
                    buscarMedicamentos(inst_SQL)
                    deleteMedicamento(inst_SQL, conn)
                elif resp == 4:
                    buscarMedicamentos(inst_SQL)

        # Cadastro de Laboratorios
        elif opc == 2:
            resp = 0

            while resp != 5:
                print("1-Inserção")
                print("2-Alteração")
                print("3-Exclusão")
                print("4-Listar todos")
                print("5-Voltar")
                try:
                    resp = int(input("Digite a opção (1-5): "))
                except ValueError:
                    print("Por favor, digite um número válido.")

                if resp == 1:
                    insertLaboratorio(inst_SQL, conn)
                elif resp == 2:
                    buscarLaboratorios(inst_SQL)
                    updateLaboratorio(inst_SQL, conn)
                elif resp == 3:
                    buscarLaboratorios(inst_SQL)
                    deleteLaboratorio(inst_SQL, conn)
                elif resp == 4:
                    buscarLaboratorios(inst_SQL)

        # Relatório de todos Medicamentos por laboratório
        elif opc == 3:
            str_consulta = """
                            SELECT m.*
                            FROM Medicamentos m
                            WHERE m.laboratorio_id = :1
                           """

            colunas = ['medicamento_id', 'laboratorio_id', 'medicamento_descricao', 'medicamento_indicacao',
                       'medicamento_valor']

            consulta_tabela(inst_SQL, str_consulta, colunas, False)

        # Relatório de todos Medicamentos do laboratório esquilhido
        # cujo valor seja maior do que 70,00.
        elif opc == 4:
            str_consulta = """
                            SELECT m.*
                            FROM Medicamentos m
                            WHERE m.laboratorio_id = :1
                            AND m.medicamento_valor > 70
                           """

            colunas = ['medicamento_id', 'laboratorio_id', 'medicamento_descricao', 'medicamento_indicacao',
                       'medicamento_valor']

            consulta_tabela(inst_SQL, str_consulta, colunas, False)

        # Relatório de todos Medicamentos do laboratório esquilhido
        # cujo valor esteja entre 100,00 e 250,00.
        elif opc == 5:
            str_consulta = """
                            SELECT m.*
                            FROM Medicamentos m
                            WHERE m.laboratorio_id = :1
                            AND m.medicamento_valor between 100.00 and 250.00
                           """

            colunas = ['medicamento_id', 'laboratorio_id', 'medicamento_descricao', 'medicamento_indicacao',
                       'medicamento_valor']

            consulta_tabela(inst_SQL, str_consulta, colunas, False)

        # Exportar relatório de todos os Medicamentos por laboratório para um arquivo TXT
        elif opc == 6:
            str_consulta = """
                            SELECT m.*
                            FROM Medicamentos m
                            WHERE m.laboratorio_id = :1
                           """

            colunas = ['medicamento_id', 'laboratorio_id', 'medicamento_descricao', 'medicamento_indicacao',
                       'medicamento_valor']

            consulta_tabela(inst_SQL, str_consulta, colunas, True)

        # Exportar relatório de todos os Medicamentos do laboratório esquilhido cujo valor seja maior do que 70,00
        elif opc == 7:
            str_consulta = """
                            SELECT m.*
                            FROM Medicamentos m
                            WHERE m.laboratorio_id = :1
                            AND m.medicamento_valor > 70
                           """

            colunas = ['medicamento_id', 'laboratorio_id', 'medicamento_descricao', 'medicamento_indicacao',
                       'medicamento_valor']

            consulta_tabela(inst_SQL, str_consulta, colunas, True)

        # Exportar relatório de todos os Medicamentos do laboratório esquilhido cujo valor esteja entre 100,00 e 250,00
        elif opc == 8:
            str_consulta = """
                            SELECT m.*
                            FROM Medicamentos m
                            WHERE m.laboratorio_id = :1
                            AND m.medicamento_valor between 100.00 and 250.00
                           """

            colunas = ['medicamento_id', 'laboratorio_id', 'medicamento_descricao', 'medicamento_indicacao',
                       'medicamento_valor']

            consulta_tabela(inst_SQL, str_consulta, colunas, True)


def insertMedicamento(inst_SQL, conn):
    try:
        med_descricao = input("Digite a descrição do remédio: ")
        med_indicacao = input("Digite a indicação: ")
        med_valor = float(input("Digite o valor do medicamento: "))

        print("\nNossos Laboratórios")
        buscarLaboratorios(inst_SQL)

        labExiste = insertLaboratorio(inst_SQL, conn)

        if labExiste is not None:
            sql_insertMed = """
                            INSERT INTO Medicamentos (laboratorio_id, medicamento_descricao, medicamento_indicacao, medicamento_valor) 
                            VALUES (:1, :2, :3, :4)
                            """
            inst_SQL.execute(sql_insertMed, (labExiste, med_descricao, med_indicacao, med_valor))

            conn.commit()
            print("Medicamento inserido com sucesso.")
        else:
            print("Falha ao inserir medicamento: Laboratório não encontrado.")

    except ValueError:
        print("Dados inválidos.")
    except Exception as e:
        print("Erro ao inserir medicamento:", e)


def updateMedicamento(inst_SQL, conn):
    try:
        medicamento_id = int(input("Digite o ID do medicamento que deseja atualizar: "))
        med_descricao = input("Digite a nova descrição do remédio: ")
        med_indicacao = input("Digite a nova indicação: ")
        med_valor = float(input("Digite o novo valor do medicamento: "))

        sql_updateMed = """
                        UPDATE Medicamentos
                        SET medicamento_descricao = :1, medicamento_indicacao = :2, medicamento_valor = :3
                        WHERE medicamento_id = :4
                        """

        inst_SQL.execute(sql_updateMed, (med_descricao, med_indicacao, med_valor, medicamento_id))

        conn.commit()
        print("Medicamento atualizado com sucesso.")

    except ValueError:
        print("Dados inválidos.")
    except Exception as e:
        print("Erro ao atualizar medicamento:", e)


def deleteMedicamento(inst_SQL, conn):
    try:
        medicamento_id = int(input("Digite o ID do medicamento que deseja excluir: "))

        sql_deleteMed = """
                        DELETE FROM Medicamentos
                        WHERE medicamento_id = :1
                        """

        inst_SQL.execute(sql_deleteMed, (medicamento_id,))

        conn.commit()
        print("Medicamento excluído com sucesso.")

    except ValueError:
        print("Dados inválidos.")
    except Exception as e:
        print("Erro ao excluir medicamento:", e)


def buscarMedicamentos(inst_SQL):
    sql_buscarMedicamentos = """
                                SELECT * FROM medicamentos
                             """

    inst_SQL.execute(sql_buscarMedicamentos)

    medicamentos = inst_SQL.fetchall()

    medicamentos.sort()

    print("ID  Lab_ID")
    for medicamento in medicamentos:
        print(medicamento)
    print("")


def insertLaboratorio(inst_SQL, conn):
    try:
        lab_cnpj = input("\nDigite o CNPJ do laboratório: ")

        sql_buscarLab = """
                        SELECT laboratorio_id FROM Laboratorios
                        WHERE laboratorio_cnpj = :1
                        """

        inst_SQL.execute(sql_buscarLab, (lab_cnpj,))

        lab_row = inst_SQL.fetchone()

        if lab_row is None:
            print("Não encontramos esse laboratório, vamos inseri-lo !!")
            lab_nome = input("Digite o nome do laboratório: ")
            lab_endereco = input("Digite o endereço do laboratório: ")

            sql_insertLab = """
                            INSERT INTO Laboratorios (laboratorio_nome, laboratorio_cnpj, laboratorio_endereco) 
                            VALUES (:1, :2, :3)
                            """

            inst_SQL.execute(sql_insertLab, (lab_nome, lab_cnpj, lab_endereco))

            conn.commit()

            inst_SQL.execute(sql_buscarLab, (lab_cnpj,))
            lab_row = inst_SQL.fetchone()
            if lab_row:
                lab_id = lab_row[0]
                print("Laboratório inserido com sucesso. ID:", lab_id)
                return lab_id
            else:
                print("Falha ao recuperar o ID do laboratório inserido.")
                return None
        else:
            lab_id = lab_row[0]
            print("Laboratório encontrado. ID:", lab_id)
            return lab_id

    except ValueError:
        print("Dados inválidos.")
    except Exception as e:
        print("Erro ao inserir laboratório:", e)


def buscarLaboratorios(inst_SQL):
    sql_buscarLaboratorios = """
                                SELECT * FROM laboratorios
                             """

    inst_SQL.execute(sql_buscarLaboratorios)

    laboratorios = inst_SQL.fetchall()

    laboratorios.sort()

    print("ID")
    for laboratorio in laboratorios:
        print(laboratorio)
    print("")


def deleteLaboratorio(inst_SQL, conn):
    try:
        laboratorio_id = int(input("Digite o ID do laboratório que deseja excluir: "))

        sql_deleteLab = """
                        DELETE FROM Laboratorios
                        WHERE laboratorio_id = :1
                        """
        inst_SQL.execute(sql_deleteLab, (laboratorio_id,))
        conn.commit()
        print("Laboratório excluído com sucesso.")
    except ValueError:
        print("Dados inválidos.")
    except Exception as e:
        print("Erro ao excluir laboratório:", e)


def updateLaboratorio(inst_SQL, conn):
    try:
        laboratorio_id = int(input("Digite o ID do laboratório que deseja atualizar: "))
        lab_nome = input("Digite o novo nome do laboratório: ")
        lab_cnpj = input("Digite o novo CNPJ do laboratório: ")
        lab_endereco = input("Digite o novo endereço do laboratório: ")

        sql_updateLab = """
                        UPDATE Laboratorios
                        SET laboratorio_nome = :1, laboratorio_cnpj = :2, laboratorio_endereco = :3
        WHERE laboratorio_id = :4
        """
        inst_SQL.execute(sql_updateLab, (lab_nome, lab_cnpj, lab_endereco, laboratorio_id))
        conn.commit()
        print("Laboratório atualizado com sucesso.")
    except ValueError:
        print("Dados inválidos.")
    except Exception as e:
        print("Erro ao atualizar laboratório:", e)


def conecta_BD():
    try:
        # conectar com o Servidor
        dnStr = oracledb.makedsn("oracle.fiap.com.br", "1521", "ORCL")
        # efetuar a conexao com o usuario
        conn = oracledb.connect(user='RM552618', password='201104', dsn=dnStr)

        inst_SQL = conn.cursor()

    except Exception as e:
        print("Erro: ", e)
        conexao = False
        inst_SQL = ""
        conn = ""
    else:
        conexao = True

    return (conexao, inst_SQL, conn)


def consulta_tabela(inst_SQL, str_consulta, colunas, gera_txt):
    lista = []

    buscarLaboratorios(inst_SQL)

    laboratorio_id = input("Digite o id do laboratório: ")

    inst_SQL.execute(str_consulta, (laboratorio_id,))

    dados = inst_SQL.fetchall()

    for registro in dados:
        lista.append(registro)

    # Ordena a lista
    lista = sorted(lista)

    # Gera um Dataframe com os dados da lista (Pandas)
    base_df = pd.DataFrame.from_records(lista, columns=colunas)

    if base_df.empty:
        print("Não há registros cadastrados.")
    else:
        if gera_txt:
            texto = base_df.to_string(index=False, columns=colunas)  # Remover o índice e exibir todas as colunas
            nome_arq = input("Digite o nome do arquivo texto a ser gerado: ")
            with open(nome_arq, "w", encoding="utf-8") as arq:
                arq.write(texto)
            print("Arquivo gerado com sucesso!")
        else:
            print(base_df)
        print("\n")


if __name__ == "__main__":
    main()
