from database.criar_tabela import criar_tabela
from models.produtos import adicionar_produto

print("ensira as informações para acessar")

while True:
    n1 = input("Nome de usuario: ")
    n2 = input("Senha: ")

    if n1 == "JulianaCabral" and n2 == "171524":
        print("iniciando sistema")
        break
    else:
        print("Usuario ou senha incorreto!")

criar_tabela()
        

def main():
    print("Menu de configuração\n")
    n1 = input("""
                1 - Produtos

                2 - Cliente

                3 - Vendas

                4 - Relatórios

                5 - Sair

                Escolha: 
                """)

    if n1 == "1":
        print("Opções de configuração do Produto")
        h1 = input("""
                    1 - Adicionar Produto
                                    
                    2 - Listar
                                    
                    3 - Alterar
                   
                    Escolha: 
                    """)
        
        if h1 == "1":
            adicionar_produto()