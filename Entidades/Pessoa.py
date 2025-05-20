from datetime import date

class Pessoa:
    _ultimo_id = 0

    def __init__(self, nome: str, sexo, nacionalidade: str, nascimento: date):
        Pessoa._ultimo_id += 1
        self.__id = Pessoa._ultimo_id
        self.__nome = nome
        self.__sexo = sexo
        self.__nacionalidade = nacionalidade
        self.__nascimento = nascimento

    @property
    def id(self):
        return self.__id

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
    
    def nomeAlterar(self, nome: str):
        self.__nome = nome

    def sexoAlterar(self, sexo: str):
        self.__sexo = sexo

    def nascimentoAlterar(self, nascimento: date):
        self.__nascimento = nascimento
    
    def nacionalidadeAlterar(self, nacionalidade: str):
        self.__nacionalidade = nacionalidade