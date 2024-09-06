SET SERVEROUTPUT ON
DECLARE

    numeroAluno NUMBER := &RA;
    nomeAluno VARCHAR2(50) := '&NOME';

BEGIN
    INSERT INTO ALUNO VALUES (numeroAluno, nomeAluno);
    
    COMMIT;
    
    SELECT 
        RA,
        NOME 
    INTO 
        numeroAluno,
        nomeAluno 
    FROM 
        ALUNO 
    WHERE 
        RA = numeroaluno;
    
    dbms_output.put_line('O código de cadastro do aluno é : '
                         || numeroaluno
                         || ' Nome completo do Aluno: '
                         || nomealuno);
END;