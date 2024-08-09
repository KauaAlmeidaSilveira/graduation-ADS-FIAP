package br.com.fiap.main;

import br.com.fiap.model.Corretora;
import br.com.fiap.sevices.CorretoraService;
import org.apache.http.ParseException;

import java.io.IOException;
import java.util.List;
import java.util.Scanner;

public class cpJavaConsumoAPI {

    public static void main(String[] args) throws ParseException, IOException {

        Scanner sc = new Scanner(System.in);

        CorretoraService corretoraService = new CorretoraService();

        System.out.print("Deseja procurar uma corretora em específico ? (S/N)");
        String resp = sc.nextLine();

        if(resp.toUpperCase().equals("S")) {
            System.out.print("""
                    Cnpj para testes: 
                    
                    02332886000104
                    17312661000155
                    75724195000111
                    85010361000171
                    99988065000154
                    
                    """);

            System.out.print("Digite o cnpj da corretora: ");
            String cnpj = sc.nextLine();

            System.out.println("\n"+corretoraService.getCorretoraWithCNPJ(cnpj));
        }else {
            List<Corretora> corretoras = corretoraService.getCorretoras();

            System.out.println("");

            corretoras.forEach(System.out::println);
        }



        sc.close();

    }

}
