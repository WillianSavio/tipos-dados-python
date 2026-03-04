
print(" === CADASTRE O PRODUTO === ")

produto = {
    "Nome": "",
    "Preco": "",
    "Quantidade em estoque": "",
    "Categoria": ""
}

produto["Nome"] = input("Qual o nome do poduto que deseja cadastrar? \n" )
produto["Preco"] = input("Qual o preço do produto? \n")
produto["Quantidade em estoque"] = input("Qual a quantidade em estoque? \n")
produto["Categoria"] = input("Qual a categoria do produto? \n")

print("\n Produto cadatrado com sucesso")

print(f"\n Nome: {produto["Nome"]}\n Preço: {produto["Preco"]}\n Estoque: {produto["Quantidade em estoque"]}\n Categoria: {produto["Categoria"]}\n")