from datetime import date

class MembroAcademia:
    _ultimo_id = 0

    def __init__(self, nome: str, nascimento: date, nacionalidade: str):
        MembroAcademia._ultimo_id += 1
        self.id = MembroAcademia._ultimo_id
        self.nome = nome
        self.nascimento = nascimento
        self.nacionalidade = nacionalidade
        self.votos_realizados = set() 