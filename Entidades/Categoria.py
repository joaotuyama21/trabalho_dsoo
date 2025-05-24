from Entidades.Funcao import Funcao
from Entidades.Participante import Participante
from Entidades.Filme import Filme

class Categoria:
    def __init__(self, nome: str, funcao: Funcao, eFilme: bool):
        self.__nome = nome
        self.__funcao = funcao
        if eFilme:
            self.__tipo = Filme("Titulo", 0, "Genero", "Sinopse")
        else:
            self.__tipo = Participante(None, None, None)

    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def funcao(self) -> str:
        return self.__funcao