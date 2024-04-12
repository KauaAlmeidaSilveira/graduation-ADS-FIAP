package br.com.fiap.main;

import br.com.fiap.model.Endereco;
import br.com.fiap.services.ViaCepService;

import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {

		ViaCepService viaCepService = new ViaCepService();

		Endereco endereco = viaCepService.getEndereco("03909080");

		System.out.println(endereco);

	}

}
