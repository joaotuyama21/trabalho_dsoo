from Entidades.Categoria import Categoria
from Limite.TelaCategoria import TelaCategoria

class ControladorCategoria:
    def __init__(self, controladorSistema):
        self.__categorias = []
        self.__telaCategoria = TelaCategoria(self)
        self.__controladorSistema = controladorSistema

    