from Entidades.Categoria import Categoria

class Funcao:
    def __init__(self, nome: str, categorias: Categoria):
        self.__nome = nome
        self.__categoria = categorias