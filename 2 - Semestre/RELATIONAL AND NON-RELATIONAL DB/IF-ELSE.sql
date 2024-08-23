SET SERVEROUTPUT ON;

DECLARE
    
    numero NUMBER := &DigiteUmNumero;
    
BEGIN

    IF mod(numero, 2) = 0 then
        dbms_output.put_line('O numero é par');
    ELSE
        dbms_output.put_line('O numero é impar');
    END IF;

END;