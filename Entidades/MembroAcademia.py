import Categoria, Indicacao, Voto
from datetime import date

class MembroAcademia:
    _ultimo_id = 0

    def __init__(self, nome: str, sexo: str,nascimento: date, nacionalidade: str, categoriasIndicacao: Categoria):
        MembroAcademia._ultimo_id += 1
        self.__id = MembroAcademia._ultimo_id
        self.__nome = nome
        self.__nascimento = nascimento
        self.__nacionalidade = nacionalidade
        self.__votosRealizados = set() 
        self.__indicacoesRealizadas = set()