SET SERVEROUTPUT ON;

DECLARE
    
    numero NUMBER := &DigiteUmNumero;
    
BEGIN

    IF mod(numero, 2) = 0 then
        dbms_output.put_line('O numero � par');
    ELSE
        dbms_output.put_line('O numero � impar');
    END IF;

END;