from database.criar_tabela import criar_tabela
from inicio import main

print("ensira as informações para acessar")

while True:
    n1 = input("Nome de usuario: ")
    n2 = input("Senha: ")

    if n1 == "ok" and n2 == "1":
        print("iniciando sistema")
        break
    else:
        print("Usuario ou senha incorreto!")

criar_tabela()
        

main()