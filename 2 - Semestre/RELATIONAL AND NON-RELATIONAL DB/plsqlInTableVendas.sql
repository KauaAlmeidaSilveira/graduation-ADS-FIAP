SELECT 
    ORDERNUMBER,
    CASE 
        WHEN DEALSIZE = 'Medium' THEN
            'Empresa de médio porte '
        WHEN DEALSIZE = 'Small' THEN
            'Empresa de pequeno porte'
        WHEN DEALSIZE = 'Large' THEN
            'Empresa de grande porte'
    END porteempresa0
FROM tb_venda;

select * from tb_venda;