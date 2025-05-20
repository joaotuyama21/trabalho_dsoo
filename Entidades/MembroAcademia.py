from Entidades.Categoria import Categoria
from Entidades.Pessoa import Pessoa
from datetime import date

class MembroAcademia(Pessoa):
    _ultimo_id = 0

    def __init__(self, nome: str, sexo: str, nascimento: date, nacionalidade: str):
        MembroAcademia._ultimo_id += 1
        self.__id = MembroAcademia._ultimo_id
        super().__init__(nome, sexo, nascimento, nacionalidade)
        self.__categoriasIndicacao = []
    
    @property
    def id(self):
        return self.__id
    
    def incluirCategoria(self, categoria: Categoria):
        self.__categoriasIndicacao.append(categoria)

    