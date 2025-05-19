from datetime import date

class Pessoa:
    def __init__(self, nome: str, sexo, nacionalidade: str, nascimento: date):
        self.__nome = nome
        self.__sexo = sexo
        self.__nacionalidade = nacionalidade
        self.__nascimento = nascimento