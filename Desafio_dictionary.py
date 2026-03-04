
print(" === CADASTRE O PRODUTO === ")

lista_produto = []

while True:

    produto = {
    "Nome": "",
    "Preco": "",
    "Quantidade em estoque": "",
    "Categoria": ""
    }

    lista_produto.append(produto)

    produto["Nome"] = input("Qual o nome do poduto que deseja cadastrar? \n" )
    produto["Preco"] = input("Qual o preço do produto? \n")
    produto["Quantidade em estoque"] = input("Qual a quantidade em estoque? \n")
    produto["Categoria"] = input("Qual a categoria do produto? \n")

    print("\n Produto cadastrado com sucesso")

    print(f"\n Nome: {produto["Nome"]}\n Preço: {produto["Preco"]}\n Estoque: {produto["Quantidade em estoque"]}\n Categoria: {produto["Categoria"]}\n")

    pergunta = input("Você deseja adicionar mais produtos? Digite S ou N")

    if pergunta.upper() != "S":
        print("Encerrando o cadastro...")
        print(lista_produto)
        break