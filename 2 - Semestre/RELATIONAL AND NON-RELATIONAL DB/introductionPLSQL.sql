SET SERVEROUTPUT ON;

DECLARE
    v_nome VARCHAR(30);
    v_idade NUMBER := 39;
    v_idade2 NUMBER := 43;
    
    slrAtual NUMBER := 1600;
    vlrDolar NUMBER := 45;
    vlrCotacao number := 5.50;
    
BEGIN
    v_nome := 'VERGILIO';
    dbms_output.put_line(v_nome || v_idade);
    dbms_output.put_line(slrAtual*1.25);
    dbms_output.put_line('$45 em reais: R$'||vlrdolar*vlrcotacao);
END;