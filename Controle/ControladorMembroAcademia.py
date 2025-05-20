from Entidades.MembroAcademia import MembroAcademia
from Limite.TelaMembroAcademia import TelaMembroAcademia
import Exceptions.MembroNaoEncontradoException

from datetime import date

class ControladorMembroAcademia():

    def __init__(self, controladorSistema):
        self.__membrosAcademia = []
        self.__controladorSistema = controladorSistema
        self.__telaMembroAcademia = TelaMembroAcademia(self)

        self.membrosAcademia.append(MembroAcademia("Matheus", "Masculino", date(2004,12,13), "Br"))

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
        lista_opcoes = {1: self.addMembro, 2: self.delMembro, 3: self.alterarMembroAcademia}

        while True:
            opcao = self.telaMembroAcademia.exibirMenuMembros()
            if opcao == 0:
                break
            funcao = lista_opcoes[opcao]
            funcao()

    def addMembro(self): 
        info = self.telaMembroAcademia.incluirMembroInfo()
        
        # Fazer verificação de membros duplicados
        novoMembro = MembroAcademia(info["nome"], info["sexo"], info["nascimento"], info["nacionalidade"])
        if not self.verificarSeHaMembroDuplicado(novoMembro):
            self.membrosAcademia.append(novoMembro)
            self.telaMembroAcademia.mostraMensagem(f"\n✅ Membro '{novoMembro.nome}' cadastrado com ID {novoMembro.id}!")
        else:
            self.telaMembroAcademia.mostraMensagem(f"\n Membro '{novoMembro.nome}' já cadastrado!")
            

    def verificarSeHaMembroDuplicado(self, copia: MembroAcademia):
        for membro in self.membrosAcademia:
            if membro.nome == copia.nome:
                return True
        return False

    # Inserir Polimorfismo em deletar e buscar (por id e nome)
    def delMembro(self):
        self.telaMembroAcademia.mostraMensagem("\n--- Remover Membro ---")
        membroRemovido = self.buscarMembroAcademia()
        self.membrosAcademia.remove(membroRemovido)
        self.telaMembroAcademia.mostraMensagem(f"\n✅ Membro '{membroRemovido.nome}' foi removdo com sucesso!")

    def alterarMembroAcademia(self):
            self.telaMembroAcademia.mostraMensagem("\n --- Alterar Membro ---")
            membroAlterar = self.buscarMembroAcademia()
            atributos = {1:"Nome", 2:"Sexo", 3:"Nacionalidade", 4:"Nascimento", 5:"Categorias"}
            nomeAtributo = self.telaMembroAcademia.alterarAtributoMembroAcademia(atributos)
            




    def buscarMembroAcademia(self):
        id = self.telaMembroAcademia.buscarMembroAcademiaInfo()
        for membro in self.membrosAcademia:
            if membro.id == id:
                return membro
                
            # raise MembroNaoEncontradoException