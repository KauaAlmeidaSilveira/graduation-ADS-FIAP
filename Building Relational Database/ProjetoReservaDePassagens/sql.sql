DROP TABLE companhia_aerea CASCADE CONSTRAINTS;
DROP TABLE passageiro CASCADE CONSTRAINTS;
DROP TABLE reserva CASCADE CONSTRAINTS;
DROP TABLE voo CASCADE CONSTRAINTS;

DELETE FROM companhia_aerea;
DELETE FROM passageiro;
DELETE FROM reserva;
DELETE FROM voo;

CREATE TABLE companhia_aerea (
    id_companhia INTEGER GENERATED ALWAYS AS IDENTITY,
    nome         VARCHAR2(100 CHAR) NOT NULL,
    pais_origem  VARCHAR2(150 CHAR) NOT NULL,
    info_contato VARCHAR2(150 CHAR) NOT NULL
);

ALTER TABLE companhia_aerea ADD CONSTRAINT companhia_aerea_pk PRIMARY KEY ( id_companhia );

CREATE TABLE passageiro (
    id_passageiro INTEGER GENERATED ALWAYS AS IDENTITY,
    nome          VARCHAR2(100 CHAR) NOT NULL,
    email         VARCHAR2(100 CHAR) NOT NULL,
    nmr_telefone  VARCHAR2(11 CHAR) NOT NULL
);

ALTER TABLE passageiro ADD CONSTRAINT passageiro_pk PRIMARY KEY ( id_passageiro );

CREATE TABLE voo (
    id_voo       INTEGER GENERATED ALWAYS AS IDENTITY,
    origem       VARCHAR2(150 CHAR) NOT NULL,
    destino      VARCHAR2(150 CHAR) NOT NULL,
    data_partida DATE NOT NULL,
    data_chegada DATE NOT NULL,
    nmr_assentos INTEGER NOT NULL,
    id_companhia INTEGER NOT NULL
);

ALTER TABLE voo ADD CONSTRAINT voo_pk PRIMARY KEY ( id_voo );

ALTER TABLE voo
    ADD CONSTRAINT voo_companhia_aerea_fk FOREIGN KEY ( id_companhia )
        REFERENCES companhia_aerea ( id_companhia );

CREATE TABLE reserva (
    id_reserva    INTEGER GENERATED ALWAYS AS IDENTITY,
    info_voo      VARCHAR2(255 CHAR) NOT NULL,
    nmr_assento   INTEGER NOT NULL,
    status        VARCHAR2(50 CHAR) NOT NULL,
    id_passageiro INTEGER NOT NULL,
    id_voo        INTEGER NOT NULL
);

ALTER TABLE reserva ADD CONSTRAINT reserva_pk PRIMARY KEY ( id_reserva );

ALTER TABLE reserva
    ADD CONSTRAINT reserva_passageiro_fk FOREIGN KEY ( id_passageiro )
        REFERENCES passageiro ( id_passageiro );

ALTER TABLE reserva
    ADD CONSTRAINT reserva_voo_fk FOREIGN KEY ( id_voo )
        REFERENCES voo ( id_voo );

ALTER TABLE reserva
    ADD CONSTRAINT reserva_status_check 
        CHECK (status = 'confirmada' OR status = 'pendente')


-------------------------------------------------------------------------------

-- COMPANHIA_AEREA
INSERT INTO companhia_aerea (nome, pais_origem, info_contato)
VALUES ('Delta Air Lines', 'Estados Unidos', 'contact@delta.com');

INSERT INTO companhia_aerea (nome, pais_origem, info_contato)
VALUES ('Singapore Airlines', 'Singapura', 'info@singaporeair.com');

INSERT INTO companhia_aerea (nome, pais_origem, info_contato)
VALUES ('Emirates', 'Emirados Árabes Unidos', 'contact@emirates.com');

-- PASSAGEIRO

INSERT INTO passageiro (nome, email, nmr_telefone)
VALUES ('João Silva', 'joao@example.com', '5551234567');

INSERT INTO passageiro (nome, email, nmr_telefone)
VALUES ('Maria Souza', 'maria@example.com', '556453453');

INSERT INTO passageiro (nome, email, nmr_telefone)
VALUES ('Carlos Ferreira', 'carlos@example.com', '5557654321');

INSERT INTO passageiro (nome, email, nmr_telefone)
VALUES ('Kauã Almeida', 'kaua@example.com', '5558765432');

-- VOO

INSERT INTO voo (origem, destino, data_partida, data_chegada, nmr_assentos, id_companhia)
VALUES ('Nova York', 'Los Angeles', TO_DATE('20-11-2004', 'dd-MM-yyyy'), TO_DATE('23-11-2004', 'dd-MM-yyyy'), 200, 1);

INSERT INTO voo (origem, destino, data_partida, data_chegada, nmr_assentos, id_companhia)
VALUES ('Australia', 'Canada', TO_DATE('25-02-2004', 'dd-MM-yyyy'), TO_DATE('26-02-2004', 'dd-MM-yyyy'), 300, 2);

INSERT INTO voo (origem, destino, data_partida, data_chegada, nmr_assentos, id_companhia)
VALUES ('Brasil', 'Nova Zelandia', TO_DATE('03-05-2004', 'dd-MM-yyyy'), TO_DATE('05-05-2004', 'dd-MM-yyyy'), 250, 3);

INSERT INTO voo (origem, destino, data_partida, data_chegada, nmr_assentos, id_companhia)
VALUES ('França', 'Portugal', TO_DATE('10-02-2004', 'dd-MM-yyyy'), TO_DATE('15-02-2004', 'dd-MM-yyyy'), 100, 1);

-- RESERVA

INSERT INTO reserva (info_voo, nmr_assento, status, id_passageiro, id_voo)
VALUES ('Voo de Nova York para Los Angeles', 25, 'confirmada', 1, 1);

INSERT INTO reserva (info_voo, nmr_assento, status, id_passageiro, id_voo)
VALUES ('Voo de Brasil para Nova Zelandia', 100, 'confirmada', 3, 3);

INSERT INTO reserva (info_voo, nmr_assento, status, id_passageiro, id_voo)
VALUES ('Voo de Australia para Canada', 299, 'confirmada', 2, 2);

INSERT INTO reserva (info_voo, nmr_assento, status, id_passageiro, id_voo)
VALUES ('Voo de França para Portugal', 17, 'pendente', 4, 4);

-- UPDATE

UPDATE voo
SET destino = 'Paraguai'
WHERE id_voo = 2;

UPDATE passageiro
SET email = 'jubiscreudo@gmail.com', nmr_telefone = '11985367845'
WHERE id_passageiro = 4;

-- DELETE

DELETE FROM passageiro WHERE id_passageiro = 1;
-- Neste caso vai dar erro, pois não posso deletar um passageiro que ja esta
-- associado a uma reserva. A reserva depende do passageiro

DELETE FROM companhia_aerea WHERE id_companhia = 2;
-- Neste caso vai dar erro, pois não posso deletar uma companhia que ja esta
-- associado a um voo. O voo depende da companhia

select * from companhia_aerea;
select * from passageiro;
select * from voo;
select * from reserva;