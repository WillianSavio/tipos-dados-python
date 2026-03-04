
print(" === CADASTRE O PRODUTO === ")

produto = {
    "Nome": "",
    "Preco": "",
    "Quantidade em estoque": "",
    "Categoria": ""
}

produto["Nome"] = input("Qual o nome do poduto que deseja cadastrar?")
produto["Preco"] = input("Qual o preço do produto?")
produto["Quantidade em estoque"] = input("Qual a quantidade em estoque?")
produto["Categoria"] = input("Qual a categoria do produto?")

print("Produto cadatrado com sucesso")

print(f" Nome: {produto["Nome"]}\n Preço: {produto["Preco"]}\n Estoque: {produto["Quantidade em estoque"]}\n Categoria: {produto["Categoria"]}\n")