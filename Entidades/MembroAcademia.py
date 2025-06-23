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
        self.__votos = {}

    @property
    def categoriasIndicacao(self):
        return self.__categoriasIndicacao

    @property
    def id(self):
        return self.__id

    def addCategoria(self, categoria: Categoria):
        self.__categoriasIndicacao.append(categoria)

    def delCategoria(self, categoria: Categoria):
        self.__categoriasIndicacao.remove(categoria)

    def jaVotouNaCategoria(self, categoria):
        return categoria.nome in self.__votos

    def registrarVoto(self, categoria, indicado):
        self.__votos[categoria.nome] = indicado
