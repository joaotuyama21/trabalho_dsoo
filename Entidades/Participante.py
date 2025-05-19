import Pessoa, Filme, Funcao

class Participante:
    def __init__(self, participante: Pessoa, filme: Filme, funcao: Funcao):
        self.__participante = participante
        self.__filme = filme
        self.__funcao = funcao
