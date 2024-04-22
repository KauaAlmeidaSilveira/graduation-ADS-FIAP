package br.com.fiap.sevices;

import br.com.fiap.model.Corretora;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import org.apache.http.HttpEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.util.EntityUtils;

import java.io.IOException;
import java.lang.reflect.Type;
import java.util.List;

public class CorretoraService {

    public List<Corretora> getCorretoras() throws IOException {

        HttpGet request = new HttpGet("https://brasilapi.com.br/api/cvm/corretoras/v1");
        CloseableHttpClient httpClient = HttpClientBuilder.create().disableRedirectHandling().build();
        CloseableHttpResponse response = httpClient.execute(request);
        HttpEntity entity = response.getEntity();
        List<Corretora> corretoras = null;

        if (entity != null) {
            String result = EntityUtils.toString(entity);
            Gson gson = new Gson();
            Type corretorasListType = new TypeToken<List<Corretora>>(){}.getType();
            // A linha acima esta criando um tipo generico para a lista de corretoras
            // O TypeToken é uma classe do GSON que permite a criação de um tipo generico
            // para a lista de corretoras
            corretoras = gson.fromJson(result, corretorasListType);
        }

        return corretoras;

    }

    public Corretora getCorretoraWithCNPJ(String cnpj) throws IOException {

        HttpGet request = new HttpGet("https://brasilapi.com.br/api/cvm/corretoras/v1/" + cnpj);
        CloseableHttpClient httpClient = HttpClientBuilder.create().disableRedirectHandling().build();
        CloseableHttpResponse response = httpClient.execute(request);
        HttpEntity entity = response.getEntity();
        Corretora corretora = null;

        if (entity != null) {
            String result = EntityUtils.toString(entity);
            Gson gson = new Gson();
            corretora = gson.fromJson(result, Corretora.class);
        }

        return corretora;

    }

}
