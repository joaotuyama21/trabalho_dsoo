import MembroAcademia, Indicacao

class Voto:
    def __init__(self, indicacao: Indicacao, membroAcademia: MembroAcademia):
        self.__membroAcademia = membroAcademia
        self.__indicacao = indicacao
