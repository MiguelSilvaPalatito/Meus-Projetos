print("ensira as informações para acessar")

while True:
    n1 = input("Nome de usuario: ")
    n2 = input("Senha: ")

    if n1 == "JulianaCabral" and n2 == "171524":
        print("iniciando sistema")
        break
    else:
        print("Usuario ou senha incorreto!")
        
print("Menu de configuração\n")
n1 = input("""1 - Produtos

2 - Cliente

3 - Vendas

4 - Relatórios

5 - Sair

Escolha: """)
