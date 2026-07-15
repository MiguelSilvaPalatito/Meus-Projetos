from database import date

class Cliente:
    def __init__(self,
        nome: str,
        cpf: str, 
        telefone: str, 
        nascimento: date,
        pontos: int = 0):
        
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.nascimento = nascimento
        self.pontos = pontos