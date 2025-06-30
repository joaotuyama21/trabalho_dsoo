from Entidades.Funcao import Funcao
from Entidades.Participante import Participante
from Entidades.Filme import Filme

class Categoria:
    def __init__(self, nome: str, funcao: Funcao, e_filme: bool):
        self.__nome = nome
        self.__funcao = funcao
        self.__e_filme = e_filme  # True para categoria de Filme

    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def funcao(self) -> Funcao:
        return self.__funcao

    @property
    def e_filme(self) -> bool:
        return self.__e_filme