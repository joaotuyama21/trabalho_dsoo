from Controle.ControladorMembroAcademia import ControladorMembroAcademia
from Controle.ControladorPessoas import ControladorPessoas
from Controle.ControladorFilmes import ControladorFilmes
from Controle.ControladorCategoria import ControladorCategoria
from Limite.TelaSistema import TelaSistema

class ControladorSistema():
    def __init__(self):
        self.__telaSistema = TelaSistema(self)
        self.__controladorMembroAcademia = ControladorMembroAcademia(self)
        self.__controladorPessoas = ControladorPessoas(self)
        self.__controladorFilmes = ControladorFilmes(self)
        self.__controladorCategorias = ControladorCategoria(self)
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
    
    @property
    def controladorFilmes(self):
        return self.__controladorFilmes
    
    @property
    def controladorCategorias(self):
        return self.__controladorCategorias

    def inicia(self):
        self.telaInicial()

    def telaInicial(self):
        listaOpcoes = {
                       1:self.controladorMembroAcademia.exibirMenu,
                       2:self.controladorPessoas.exibirMenu,
                       3:self.controladorFilmes.exibirMenu,
                       4:self.controladorCategorias.exibirMenu
                      }

        while True:
            opcao = self.telaSistema.exibirMenuPrincipal()
            if opcao in listaOpcoes.keys():
                funcao = listaOpcoes[opcao]
                funcao()
            else: 
                self.telaSistema.mostraMensagem("Opção não encontrada. Tente novamente!")

    def adicionarPessoa(self, novaPessoa):
        self.controladorPessoas.pessoas.append(novaPessoa)