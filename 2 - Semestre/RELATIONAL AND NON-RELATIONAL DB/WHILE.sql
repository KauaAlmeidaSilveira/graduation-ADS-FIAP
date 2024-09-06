SET SERVEROUTPUT ON
DECLARE

    v_contador number(2):= 1;

BEGIN
    WHILE v_contador <= 20 LOOP
        dbms_output.put_line(v_contador);
        v_contador := v_contador + 1;
    END LOOP;
END;