from ControladorMembroAcademia import *
from Limite.TelaSistema import *

class ControladorSistema():
    def __init__(self):
        self.__controladorMembroAcademia = ControladorMembroAcademia(self)
        # Colocar os demais controladores
        self.__telaSistema = TelaSistema(self)
    
    @property
    def controladorMembroAcademia(self):
        return self.__controladorMembroAcademia

    @property
    def telaSistema(self):
        return self.__telaSistema

    def inicia(self):
        self.telaInicial()

    def telaInicial(self):
        lista_opcoes = {1:self.membros}

        while True:
            opcao = self.telaSistema.exibirMenuPrincipal()
            funcao = lista_opcoes[opcao]
            funcao()

    def menuMembros(self):
        self.controladorMembroAcademia.exibirMenuMembros()