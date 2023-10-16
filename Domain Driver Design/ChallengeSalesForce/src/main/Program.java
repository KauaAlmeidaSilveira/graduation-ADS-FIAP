package main;

import model.Entity.Cadastro.Conta;
import model.Entity.Cadastro.Empresa;
import model.Entity.Cadastro.Endereco;
import model.Entity.Cadastro.Pessoa;
import model.Entity.Servico.Pagamento;
import model.Entity.Servico.Servico;

import java.time.LocalDateTime;

public class Program {
    public static void main(String[] args) {

        Empresa emp = new Empresa("UniDrummond", "Ti");
        Endereco end = new Endereco("Rua Teste", "São Paulo", "SP", "09999999", "BR");

        Pessoa p1 = new Pessoa("Kauã", "kiwi", "9999-9999", "+55 (11) 999999999", "55.555.555-5", emp, end);

        Conta conta = new Conta("kaua@gmail.com", "321123", p1);
        Pagamento pag = new Pagamento(LocalDateTime.now(), 1780.00, "Cartão de debito", 3, "Serviço de IA");

        conta.addServico(new Servico("IAEinstein", "Serviço de IA", "IA",  pag));
        conta.addServico(new Servico("360", "Serviço geral", "Geral",  pag));
        conta.addServico(new Servico("Sales", "Serviço de vendas", "Vendas",  pag));

        System.out.println(p1);

        System.out.println(conta);
        System.out.println();

        System.out.println("------ Todos Serviços ------\n");
        System.out.println(conta.listServicos());

        System.out.println("------ Um Serviço ------");
        System.out.println(conta.getServicoByName("Sales"));

        conta.delServiceByName("360");

        System.out.println("------ Todos Serviços ------\n");
        System.out.println(conta.listServicos());
    }
}
