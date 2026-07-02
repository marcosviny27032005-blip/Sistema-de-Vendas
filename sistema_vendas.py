from statistics import quantiles

estoque_sistema = {
    1 : { "Chocolate": "Chocolate 823 Callebaut 2.5kg", "Preço": 395.00, "Quantidade" : 180},
    2 : { "Chocolate": "Chocolate Nobre Sicao ao Leite 1kg", "Preço": 215.00,"Quantidade" : 255 },
    3 : { "Chocolate": "Mycryo 500g", "Preço": 689.00, "Quantidade": 100 },
    4 : { "Açucar de Confeiteiro": "Açucar de Confeiteiro 1kg Arcolor", "Preço" : 29.99,"Qauantidade":89 },
    5 : { "Chocobol": "Chocobool 500g Mavalerio", "Preço" : 26.99, "Quantidade": 16 },
    6 : { "Glucose": "Glucose Liquida mix 500g", "Preço" : 21.00 , "Quantidade": 80 },
    7 : { "Corante": "Corante Liquido Power Glow 25g", "Preço": 7.99,"Quantidade": 60 },
    8 : { "Pó decorativo": "Pó para decoração 5g dourado mix","Preçio": 10.99, "Quantidade": 180 }
}
carrinho =[]

print("🌟"*32)
print("☆*: .｡. o(≧▽≦)o .｡.:*☆SEJA BEM VINDO A MINHA CONFEITARIA ╰(*°▽°*)╯")
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
        for chave, valor in estoque_sistema.items():
            print(f"{chave}:{valor}")
    elif opcao == 2:
        print("Adicionando Itens ao Carrinho!")
        id_produto = int(input("Qual ID Produto você deseja Comprar? "))
        if id_produto in estoque_sistema:
            qtd_produto = int(input("Quantas unidades você Deseja?: "))
            if qtd_produto <= 0:
                print("Quantidade Invalida!")
            elif qtd_produto <= estoque_sistema [id_produto]["quantidade"]:

                carrinho.append(estoque_sistema[id_produto])
                estoque_sistema[id_produto]["quantidade"] -= qtd_produto
    elif opcao == 3:
        print("Visulaizando Carrinho!")
    elif opcao == 4:
        print("Finalizar Compra")
    elif opcao == 0:
        print("Saindo...")
        break
    else:
        print("Opção Invalida")