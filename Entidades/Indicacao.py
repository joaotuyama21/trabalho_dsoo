from Entidades.Categoria import Categoria
from Entidades.MembroAcademia import MembroAcademia

class Indicacao:
    def __init__(self, indicado, categoria: Categoria, membroAcademia: MembroAcademia):
        self.__categoria = categoria
        self.__indicado = indicado
        self.__membroAcademia = membroAcademia