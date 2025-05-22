class Filme:
    def __init__(self, titulo: str, ano: int, genero: str, sinopse: str):
        self.__titulo = titulo
        self.__ano = ano
        self.__sinopse = sinopse
        self.__genero = genero

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def sinopse(self):
        return self.__sinopse
    
    @property
    def genero(self):
        return self.__genero
    
