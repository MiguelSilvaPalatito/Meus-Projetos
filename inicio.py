from models.produtos import adicionar_produto, listar_produtos, alterar

def main():
    while True:
        print("Menu de configuração\n")
        n1 = input("""
1 - Produtos

2 - Cliente

3 - Vendas

4 - Relatórios

5 - Sair

Escolha: """)

        if n1 == "1":
            while True:
                print("Opções de configuração do Produto")
                h1 = input("""
1 - Adicionar Produto
                                            
2 - Listar Produtos
                                            
3 - Alterar Produto
                        
4 - sair
                        
Escolha: """)
                
                if h1 == "1":
                    adicionar_produto()

                elif h1 == "2":
                    listar_produtos()

                elif h1 == "3":
                    alterar()

                elif h1 == "4":
                    break

                else:
                    print("opção invalida!")
