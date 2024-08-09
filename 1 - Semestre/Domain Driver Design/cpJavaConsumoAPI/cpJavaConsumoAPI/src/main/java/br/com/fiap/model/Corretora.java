package br.com.fiap.model;

public class Corretora {

    private String bairro;
    private String cep;
    private String cnpj;
    private String codigo_cvm;
    private String complemento;
    private String data_inicio_situacao;
    private String data_patrimonio_liquido;
    private String data_registro;
    private String email;
    private String logradouro;
    private String municipio;
    private String nome_social;
    private String nome_comercial;
    private String pais;
    private String status;
    private String telefone;
    private String type;
    private String uf;
    private String valor_patrimonio_liquido;

    public Corretora() {
    }

    public Corretora(String bairro, String cep, String cnpj, String codigo_cvm, String complemento, String data_inicio_situacao,
                     String data_patrimonio_liquido, String data_registro, String email, String logradouro,
                     String municipio, String nome_social, String nome_comercial, String pais, String status,
                     String telefone, String type, String uf, String valor_patrimonio_liquido) {
        this.bairro = bairro;
        this.cep = cep;
        this.cnpj = cnpj;
        this.codigo_cvm = codigo_cvm;
        this.complemento = complemento;
        this.data_inicio_situacao = data_inicio_situacao;
        this.data_patrimonio_liquido = data_patrimonio_liquido;
        this.data_registro = data_registro;
        this.email = email;
        this.logradouro = logradouro;
        this.municipio = municipio;
        this.nome_social = nome_social;
        this.nome_comercial = nome_comercial;
        this.pais = pais;
        this.status = status;
        this.telefone = telefone;
        this.type = type;
        this.uf = uf;
        this.valor_patrimonio_liquido = valor_patrimonio_liquido;
    }

    public String getBairro() {
        return bairro;
    }

    public void setBairro(String bairro) {
        this.bairro = bairro;
    }

    public String getCep() {
        return cep;
    }

    public void setCep(String cep) {
        this.cep = cep;
    }

    public String getCnpj() {
        return cnpj;
    }

    public void setCnpj(String cnpj) {
        this.cnpj = cnpj;
    }

    public String getCodigo_cvm() {
        return codigo_cvm;
    }

    public void setCodigo_cvm(String codigo_cvm) {
        this.codigo_cvm = codigo_cvm;
    }

    public String getComplemento() {
        return complemento;
    }

    public void setComplemento(String complemento) {
        this.complemento = complemento;
    }

    public String getData_inicio_situacao() {
        return data_inicio_situacao;
    }

    public void setData_inicio_situacao(String data_inicio_situacao) {
        this.data_inicio_situacao = data_inicio_situacao;
    }

    public String getData_patrimonio_liquido() {
        return data_patrimonio_liquido;
    }

    public void setData_patrimonio_liquido(String data_patrimonio_liquido) {
        this.data_patrimonio_liquido = data_patrimonio_liquido;
    }

    public String getData_registro() {
        return data_registro;
    }

    public void setData_registro(String data_registro) {
        this.data_registro = data_registro;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getLogradouro() {
        return logradouro;
    }

    public void setLogradouro(String logradouro) {
        this.logradouro = logradouro;
    }

    public String getMunicipio() {
        return municipio;
    }

    public void setMunicipio(String municipio) {
        this.municipio = municipio;
    }

    public String getNome_social() {
        return nome_social;
    }

    public void setNome_social(String nome_social) {
        this.nome_social = nome_social;
    }

    public String getNome_comercial() {
        return nome_comercial;
    }

    public void setNome_comercial(String nome_comercial) {
        this.nome_comercial = nome_comercial;
    }

    public String getPais() {
        return pais;
    }

    public void setPais(String pais) {
        this.pais = pais;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getTelefone() {
        return telefone;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getUf() {
        return uf;
    }

    public void setUf(String uf) {
        this.uf = uf;
    }

    public String getValor_patrimonio_liquido() {
        return valor_patrimonio_liquido;
    }

    public void setValor_patrimonio_liquido(String valor_patrimonio_liquido) {
        this.valor_patrimonio_liquido = valor_patrimonio_liquido;
    }

    @Override
    public String toString() {
        return "Corretora\n" +
                "Bairro: " + bairro + "\n" +
                "Cep: " + cep + "\n" +
                "CNPJ: " + cnpj + "\n" +
                "Código CVM: " + codigo_cvm + "\n" +
                "Complemento: " + complemento + "\n" +
                "Data de Início da Situação: " + data_inicio_situacao + "\n" +
                "Data do Patrimônio Líquido: " + data_patrimonio_liquido + "\n" +
                "Data do Registro: " + data_registro + "\n" +
                "Email: " + email + "\n" +
                "Logradouro: " + logradouro + "\n" +
                "Município: " + municipio + "\n" +
                "Nome Social: " + nome_social + "\n" +
                "Nome Comercial: " + nome_comercial + "\n" +
                "País: " + pais + "\n" +
                "Status: " + status + "\n" +
                "Telefone: " + telefone + "\n" +
                "Tipo: " + type + "\n" +
                "UF: " + uf + "\n" +
                "Valor do Patrimônio Líquido: " + valor_patrimonio_liquido + "\n";
    }
}
