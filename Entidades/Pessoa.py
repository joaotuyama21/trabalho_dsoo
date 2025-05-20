from datetime import date

class Pessoa:
    def __init__(self, nome: str, sexo, nacionalidade: str, nascimento: date):
        self.__nome = nome
        self.__sexo = sexo
        self.__nacionalidade = nacionalidade
        self.__nascimento = nascimento

    @property
    def nome(self):
        return self.__nome
    
    @property
    def sexo(self):
        return self.__sexo
    
    @property
    def nacionalidade(self):
        return self.__nacionalidade
    
    @property
    def nascimento(self):
        return self.__nascimento