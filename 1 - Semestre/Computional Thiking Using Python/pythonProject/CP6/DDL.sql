SELECT * FROM laboratorios;
SELECT * FROM medicamentos;

CREATE TABLE Laboratorios (
    laboratorio_id NUMBER GENERATED ALWAYS AS IDENTITY,
    laboratorio_nome VARCHAR2(100),
    laboratorio_cnpj VARCHAR2(14),
    laboratorio_endereco VARCHAR2(100)
);

ALTER TABLE Laboratorios
ADD CONSTRAINT PK_Laboratorios PRIMARY KEY (laboratorio_id);

CREATE TABLE Medicamentos (
    medicamento_id NUMBER GENERATED ALWAYS AS IDENTITY,
    laboratorio_id NUMBER NOT NULL,
    medicamento_descricao VARCHAR2(70),
    medicamento_indicacao VARCHAR2(100),
    medicamento_valor FLOAT
);

ALTER TABLE Medicamentos
ADD CONSTRAINT PK_Medicamentos PRIMARY KEY (medicamento_id);

ALTER TABLE Medicamentos
ADD CONSTRAINT FK_LABORATORIO
FOREIGN KEY (laboratorio_id)
REFERENCES Laboratorios(laboratorio_id);