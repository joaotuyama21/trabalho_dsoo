import ControladorSistema
from Entidades import MembroAcademia
from Limite import TelaMembroAcademia

class ControladorMembroAcademia():

    def __init__(self, controladorSistema: ControladorSistema):
        self.__membrosAcademia = []
        self.__controladorSistema = controladorSistema
        self.__telaMembroAcademia = TelaMembroAcademia(self)

    @property
    def membrosAcademia(self):
        return self.__membrosAcademia
    
    @property
    def controladorSistema(self):
        return self.__controladorSistema
    
    @property
    def telaMembroAcademia(self):
        return self.__telaMembroAcademia
    
    def exibirMenuMembros(self):
        lista_opcoes = {1: self.incluirMembro, 2: self.removerMembro, 3: self.listarMembros}

        while True:
            opcao = self.telaMembroAcademia.exibirMenuMembros()
            if opcao == 0:
                break
            funcao = lista_opcoes[opcao]
            funcao()

    def addMembro(self): 
        while True:
            info = self.telaMembroAcademia.incluirMembroInfo()
            
            # Fazer verificação de membros duplicados
            # Pensar num dicionario para infos
            novo_membro = MembroAcademia(info[0], info[1]. info[2])
            self.membrosAcademia.append(novo_membro)
            print(f"\n✅ Membro '{novo_membro.nome}' cadastrado com ID {novo_membro.id}!")


    # Inserir Polimorfismo em deletar e buscar (por id e nome)
    def delMembro(self):
        while True:
            id = self.telaMembroAcademia.delMembroInfo()
            for membro in self.membrosAcademia:
                if membro.id == id:
                    return self.membrosAcademia.pop(membro)
            # raise MembroNaoEncontradoException

    def buscarMembroAcademia(self):
        while True:
            id = self.telaMembroAcademia.buscarMembroAcademiaPeloId()
            for membro in self.membrosAcademia:
                if membro.id == id:
                    return membro
            # raise MembroNaoEncontradoException