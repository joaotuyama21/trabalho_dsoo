from Entidades.Pessoa import Pessoa
from Entidades.Filme import Filme
from Entidades.Funcao import Funcao

class Participante:
    def __init__(self, participante: Pessoa, filme: Filme, funcao: Funcao):
        self.__participante = participante
        self.__filme = filme
        self.__funcao = funcao
