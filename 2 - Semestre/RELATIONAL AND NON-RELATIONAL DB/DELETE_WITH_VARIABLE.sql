SET SERVEROUTPUT ON
DECLARE

    numeroAluno NUMBER := &RA;
    nomeAluno VARCHAR2(50);

BEGIN
    DELETE FROM ALUNO
    WHERE ra = numeroaluno;
    
    COMMIT;

    
END;
/

SELECT * FROM ALUNO;