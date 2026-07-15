from .conexao import conectar

def criar_tabela():
    with conectar() as conexao:
        cursor = conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE,
        preco INTEGER NOT NULL CHECK (preco > 0),
        estoque INTEGER NOT NULL CHECK (estoque >= 0),
        ativo BOOLEAN NOT NULL DEFAULT 1)""")