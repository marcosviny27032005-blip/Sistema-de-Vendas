subtotal = 0
estoque_sistema = {
    1 : { "nome": "chocolate 823 callebaut 2.5kg", "preco": 395.00, "quantidade" : 180},
    2 : { "nome": "chocolate nobre sicao ao leite 1kg", "preco": 215.00,"quantidade" : 255 },
    3 : { "nome": "mycryo 500g", "preco": 689.00, "quantidade": 100 },
    4 : { "nome": "acucar de confeiteiro 1kg arcolor", "preco" : 29.99,"quantidade":89 },
    5 : { "nome": "chocobool 500g mavalerio", "preco" : 26.99, "quantidade": 16 },
    6 : { "nome": "glucose liquida mix 500g", "preco" : 21.00 , "quantidade": 80 },
    7 : { "nome": "corante liquido power glow 25g", "preco": 7.99,"quantidade": 60 },
    8 : { "nome": "po para decoração 5g dourado mix","preco": 10.99, "quantidade": 180 }
}
carrinho =[]

print("🌟"*32)
print("☆*: .｡. o(≧▽≦)o .｡.:*☆SEJA BEM VINDO A MINHA CONFEITARIA🍫 ╰(*°▽°*)╯")
print("🌟"*32)
while True:
    print(" [1] Visualizar estoque.")
    print(" [2] Adicionar item ao carrinho.")
    print(" [3] Visualizar carrinho.")
    print(" [4] Finalizar compra.")
    print(" [0] Sair do sistema.")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Visualizando Estoque!")
        print(f"{'ID':<5}|{'NOME':<35}|{'VALOR':<10}|QUANTIDADE")
        for k, v in estoque_sistema.items():
            print(f"{k:<5}|{v["nome"]:<35}|{v["preco"]:<10}|{v["quantidade"]} ")
    elif opcao == 2:
        print("Adicionando Itens ao Carrinho!")
        id_produto = int(input("Qual ID Produto você deseja Comprar? "))
        if id_produto in estoque_sistema:
            qtd_produto = int(input("Quantas unidades você Deseja?: "))
            if qtd_produto <= 0:
                print("Quantidade Invalida!")
            elif qtd_produto <= estoque_sistema[id_produto]["quantidade"]:
                item = {
                "qtd" : qtd_produto,
                "nome" : estoque_sistema[id_produto]["nome"],
                "preco" : estoque_sistema[id_produto]["preco"],
                "preco_total": qtd_produto * estoque_sistema[id_produto]["preco"]
                }
                carrinho.append(item)
                estoque_sistema[id_produto]["quantidade"] -= qtd_produto
                print(item)
            else:
                print(f"Quantidades indisponivel, temos apenas {estoque_sistema[id_produto]["quantidade"]} unidades no estoque.")

    elif opcao == 3:
        print("Visulaizando Carrinho!")

        for i in carrinho:
            print(f"{i["quantidade"]}x {i["nome"]} no valor de R${i["preco"]}(cada)\n Total R${i["preco_total"]}")
            subtotal += i["preco_total"]
            print(f"Subtotal da Compra R${subtotal}")

    elif opcao == 4:
       print("Finalizando Compra")
       cupom = input("Digite o Nome do cupom🏷️")
       if estoque_sistema:
           while estoque_sistema:
               print(" [1] cartao debito."),
               print(" [2] cartao credito."),
               print(" [3] pix."),
               print(" [4] inserir cupom."),
               print(" [5] dinheiro.")


    elif opcao == 0:
        print("Saindo...")
        break
    else:
        print("Opção Invalida")