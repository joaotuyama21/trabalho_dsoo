from Controle.ControladorMembroAcademia import ControladorMembroAcademia
from Controle.ControladorPessoas import ControladorPessoas
from Limite.TelaSistema import TelaSistema

class ControladorSistema():
    def __init__(self):
        self.__telaSistema = TelaSistema(self)
        self.__controladorMembroAcademia = ControladorMembroAcademia(self)
        self.__controladorPessoas = ControladorPessoas(self)
        # Colocar os demais controladores
        
    @property
    def telaSistema(self):
        return self.__telaSistema
    
    @property
    def controladorMembroAcademia(self):
        return self.__controladorMembroAcademia
    
    @property
    def controladorPessoas(self):
        return self.__controladorPessoas

    def inicia(self):
        self.telaInicial()

    def telaInicial(self):
        listaOpcoes = {1:self.controladorMembroAcademia.exibirMenuMembros, 2:self.controladorPessoas.exibirMenu}

        while True:
            opcao = self.telaSistema.exibirMenuPrincipal()
            if opcao in listaOpcoes.keys():
                funcao = listaOpcoes[opcao]
                funcao()
            else: 
                self.telaSistema.mostraMensagem("Opção não encontrada. Tente novamente!")