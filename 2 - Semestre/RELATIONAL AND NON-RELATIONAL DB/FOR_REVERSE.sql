SET SERVEROUTPUT ON
BEGIN
    FOR v_contador in reverse 1..20 LOOP
        dbms_output.put_line(v_contador);
    END LOOP;
END;