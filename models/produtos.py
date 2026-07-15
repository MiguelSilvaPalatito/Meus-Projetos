from database.conexao import conectar
from gym_manager.main import main

class Produto:
    def __init__(self, nome, preco, estoque):
        if preco <= 0:
            raise ValueError("Valor Invalido")
        if estoque <= 0:
            raise ValueError("Valor Invalido")
        self.nome = nome
        self.preco = preco
        self.estoque = estoque





def converter_preco(preco):
    preco = preco.replace(",", ".")

    if "." in preco:
        reais, centavos = preco.split(".")
        centavos = centavos.ljust(2, "0")[:2]
        return int(reais + centavos)

    return int(preco + "00")





def adicionar_produto():
    nome = input("Nome: ")
    while True:
        try:
            preco = converter_preco(input("Preço: "))
            break
        except ValueError:
            print("Valor invalido!")

    
    estoque = int(input("Estoque: "))

    produto = Produto(nome, preco, estoque)

    def salvar_produto(produto):
            with conectar() as conexao:
                cursor = conexao.cursor()
                            
                cursor.execute("""INSERT INTO Produtos(nome, preco, estoque)
                            VALUES (?, ?, ?)
                            """,
                (
                    produto.nome,
                    produto.preco,
                    produto.estoque
                )
                )

    salvar_produto(produto)





def listar_produtos():
    with conectar() as conexao:
        cursor = conexao.cursor()

        cursor.execute("""
                        SELECT * FROM Produtos
                        """)
    
        produtos = cursor.fetchall()

    for produto in produtos:
        print(f"""
                ID: {produto[0]}
                Nome: {produto[1]}
                Preço: R${produto[2] / 100:.2f}
                Estoque: {produto[3]}
                ---------------------
                """)





def alterar():
    while True:
        n1 = input("""
                    Digite o numero da opção que deseja alterar

                    1 - Alterar Nome
                                
                    2 - Alterar Preço
                                
                    3 - Alterar Quantidade/Estoque
                
                    4 - sair
                                
                    Opção: 
                    """)

        if n1 == "1":
            while True:
                with conectar() as conexao:
                    cursor = conexao.cursor()

                    cursor.execute("""SELECT id, nome FROM Produtos""")

                    produtos = cursor.fetchall()

                print("Nomes atuais")

                for produto in produtos:
                    print(f"""
                            ID: {produto[0]} 
                            Nome: {produto[1]}
                            """)
                
                while True:
                    h1 = input("Digite o ID do produto que deseja mudar: ")

                    if any(str(produto[0]) == h1 for produto in produtos):
                        break
                    else:
                        print("Id de produto não encontrado!")


                while True:
                    h2 = input("Escreva o novo nome do produto: ")

                    while True:
                        ok = False
                        h3 = input("Tem certeza que deseja renomear para esse nome? s/n: ")

                        if h3.lower() == "n":
                            break
                        elif h3.lower() == "s":
                            ok = True
                            break
                        else:
                            print("Resposta invalida!")

                    if ok:
                        break
                
                with conectar() as conexao:
                    cursor = conexao.cursor()

                    cursor.execute("""
                                    UPDATE Produtos
                                    SET nome = ?
                                    WHERE id = ?;
                                    """, (h2, h1))
                print("Nome atualizado com sucesso!")

                while True:
                    ok = False
                    n2 = input("Deseja alterar algum nome novamente? s/n: ").lower()

                    if n2 == "s":
                        break
                    elif n2 == "n":
                        ok = True
                        break
                    else:
                        print("resposta invalida digite novamente!")

                if ok:
                    break


        elif n1 == "2":
            while True:
                with conectar() as conexao:
                    cursor = conexao.cursor()

                    cursor.execute("""SELECT id, nome, preco FROM Produtos""")

                    produtos = cursor.fetchall()

                print("Nomes atuais e preços")

                for produto in produtos:
                    print(f"""
                            ID: {produto[0]} 
                            Nome: {produto[1]}
                            Preço R$: {produto[2] / 100:.2f}
                            """)
                
                while True:
                    h1 = input("Digite o ID do produto que deseja mudar o preço: ")

                    if any(str(produto[0]) == h1 for produto in produtos):
                        break
                    else:
                        print("Id de produto não encontrado!")


                while True:
                    h2 = converter_preco(input("Escreva o novo preço do produto: "))
                    

                    while True:
                        ok = False
                        h3 = input("Tem certeza que deseja colocar esse valor? s/n: ")

                        if h3.lower() == "n":
                            break
                        elif h3.lower() == "s":
                            ok = True
                            break
                        else:
                            print("Resposta invalida!")

                    if ok:
                        break
                
                with conectar() as conexao:
                    cursor = conexao.cursor()

                    cursor.execute("""
                                    UPDATE Produtos
                                    SET preco = ?
                                    WHERE id = ?;
                                    """, (h2, h1))
                print("Preço atualizado com sucesso!")

                while True:
                        ok = False
                        n2 = input("Deseja alterar algum novo preço novamente? s/n: ").lower()

                        if n2 == "s":
                            break
                        elif n2 == "n":
                            ok = True
                            break
                        else:
                            print("resposta invalida digite novamente!")

                if ok:
                    break

        elif n1 == "3":
            while True:
                with conectar() as conexao:
                    cursor = conexao.cursor()

                    cursor.execute("""SELECT id, nome, estoque FROM Produtos""")

                    produtos = cursor.fetchall()

                print("Nomes atuais e quantidade")

                for produto in produtos:
                    print(f"""
                            ID: {produto[0]} 
                            Nome: {produto[1]}
                            Quantidade em estoque: {produto[3]}
                            """)
                
                while True:
                    h1 = input("Digite o ID do produto que deseja mudar a quantidade no estoque: ")

                    if any(str(produto[0]) == h1 for produto in produtos):
                        break
                    else:
                        print("Id de produto não encontrado!")


                while True:
                    h2 = converter_preco(input("Escreva a nova quantidade de estoque do produto: "))
                    

                    while True:
                        ok = False
                        h3 = input("Tem certeza que deseja colocar esse valor? s/n: ")

                        if h3.lower() == "n":
                            break
                        elif h3.lower() == "s":
                            ok = True
                            break
                        else:
                            print("Resposta invalida!")

                    if ok:
                        break
                
                with conectar() as conexao:
                    cursor = conexao.cursor()

                    cursor.execute("""
                                    UPDATE Produtos
                                    SET estoque = ?
                                    WHERE id = ?;
                                    """, (h2, h1))
                print("Estoque atualizado com sucesso!")

                while True:
                    ok = False
                    n2 = input("Deseja alterar alguma quantidade do estoque novamente? s/n: ").lower()

                    if n2 == "s":
                        break
                    elif n2 == "n":
                        ok = True
                        break
                    else:
                        print("resposta invalida digite novamente!")

                if ok:
                    break

        elif n1 == "4":
            return main()
            

        else:
            print("Numero de opção invalida digite novamente!")


