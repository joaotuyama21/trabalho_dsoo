class Categoria:
    def __init__(self, nome: str, funcao: str):
        self.__nome = nome
        self.__funcao = funcao

    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def funcao(self) -> str:
        return self.__funcao