import sqlite3

class Produto:
    def __init__(self, nome, preco, estoque):
        if preco <= 0:
            raise ValueError("Valor Invalido")
        if estoque <= 0:
            raise ValueError("Valor Invalido")
        self.nome = nome
        self.preco = preco
        self.estoque = estoque



def adicionar_produto():
    nome = input("Nome: ")
    preco = int(input("Valor: "))
    estoque = int(input("Estoque: "))

    produto = Produto(nome, preco, estoque)

#obs: no preço fazer com que o preço seja divido por 100 pois n haver virgula na hora de guardar

def salvar_produto(produto):
    with sqlite3.connect("tabelas_da_mamae.db") as conexao:
        cursor = conexao.cursor()
                       
        cursor.execut("""INSERT INTO Produtos(nome, preco, estoque)
        VALUES (?, ?, ?)""",
        (
            produto.nome,
            produto.preco,
            produto.estoque
        )
        )