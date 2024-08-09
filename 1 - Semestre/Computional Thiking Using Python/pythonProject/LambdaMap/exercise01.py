print((lambda x: x * -1)(2))
print((lambda x: 1 / x)(2))
print((lambda x: x / 2)(10))
print((lambda x, y: x ** 2 + y ** 2)(2, 5))
pessoa = {
    'nome': 'João',
    'idade': 17,
    'salario': 1000
}
(lambda x: print(f"Nome: {x['nome']}\nIdade: {x['idade']}"))(pessoa)

(lambda vlr: print(0) if vlr % 2 == 0 else print(1))(6)

(lambda x: print("Maior de idade") if x["idade"] >= 18 else print("Menor de idade"))(pessoa)

lista_dicionarios = [
    {"nome": f"Produto {i + 1}", "preco": (i + 1) * 10} for i in range(10)
]

lista_com_desconto = list(map(lambda x: {"nome": x["nome"], "preco": x["preco"] * 0.8}, lista_dicionarios))

for dicionario in lista_com_desconto:
    print(dicionario)


