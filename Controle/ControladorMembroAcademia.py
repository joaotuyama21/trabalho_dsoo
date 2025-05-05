from ControladorSistema import ControladorSistema
from Entidades.MembroAcademia import MembroAcademia
from Limite.TelaMembrosAcademia import TelaMembrosAcademia

class ControladorMembroAcademia():

    def __init__(self, controladorSistema: ControladorSistema):
        self.__membrosAcademia = []
        self.__controladorSistema = controladorSistema
        self.__telaMembrosAcademia = TelaMembrosAcademia(self)

    @property
    def membrosAcademia(self):
        return self.__membrosAcademia
    
    @property
    def controladorSistema(self):
        return self.__controladorSistema
    
    @property
    def telaMembrosAcademia(self):
        return self.__telaMembrosAcademia
    
    def exibir_menu_membros(self):
        lista_opcoes = {1: self.incluir_membro, 2: self.remover_membro, 3: self.listar_membros}

        while True:
            opcao = self.telaMembrosAcademia.exibir_menu_membros()
            if opcao == 0:
                break
            funcao = lista_opcoes[opcao]
            funcao()

    def incluir_membro(self): 
        while True:
            info = TelaMembrosAcademia.incluir_membro_info()
            
            # Fazer verificação de membros duplicados
            # Pensar num dicionario para infos
            novo_membro = MembroAcademia(info[0], info[1]. info[2])
            self.membrosAcademia.append(novo_membro)
            print(f"\n✅ Membro '{novo_membro.nome}' cadastrado com ID {novo_membro.id}!")
