select * from t_sip_funcionario;

select * from t_sip_depto;

select func.nm_funcionario, dep.nm_depto
from t_sip_funcionario func 
INNER JOIN t_sip_depto dep
on func.cd_depto = dep.cd_depto;

select * from t_sip_execucao_proj;

select * from t_sip_projeto;

select func.cd_func, func.nm_funcionario, proj.dt_inicio, exec_proj.ds_papel_func_proj
from t_sip_funcionario func 
INNER JOIN t_sip_execucao_proj exec_proj
on func.cd_func = exec_proj.cd_func
INNER JOIN t_sip_projeto proj
on exec_proj.cd_projeto = proj.cd_projeto
order by func.nm_funcionario;


select * from t_sip_dependente;

select f.nm_funcionario, d.nm_dependente
from t_sip_funcionario f
inner join t_sip_dependente d
on f.cd_func = d.cd_func;

select f.nm_funcionario, d.nm_dependente
from t_sip_funcionario f
left join t_sip_dependente d
on f.cd_func = d.cd_func
where d.cd_func is null
order by f.nm_funcionario;
