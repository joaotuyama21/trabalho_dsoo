from Entidades.MembroAcademia import MembroAcademia
from Limite.TelaMembroAcademia import TelaMembroAcademia
from Controle.ControladorPessoas import ControladorPessoas

from datetime import date

class ControladorMembroAcademia():

    def __init__(self, controladorSistema):
        self.__membrosAcademia = []
        self.__controladorSistema = controladorSistema
        self.__telaMembroAcademia = TelaMembroAcademia(self)

        #self.membrosAcademia.append(MembroAcademia("Matheus", "Masculino", date(2004,12,13), "Br"))

    @property
    def controladorPesoas(self):
        return self.__controladorPessoas

    @property
    def membrosAcademia(self):
        return self.__membrosAcademia
    
    @property
    def controladorSistema(self):
        return self.__controladorSistema
    
    @property
    def telaMembroAcademia(self):
        return self.__telaMembroAcademia
    
    def exibirMenu(self):
        lista_opcoes = {1: self.addMembro, 2: self.delMembro, 3: self.listarMembros, 4: self.indicar}

        while True:
            opcao = self.telaMembroAcademia.exibirMenuMembros()
            if opcao == 0:
                break
            funcao = lista_opcoes[opcao]
            funcao()

    def addMembro(self): 
        info = self.telaMembroAcademia.incluirMembroInfo()
        novoMembro = MembroAcademia(info["nome"], info["sexo"], info["nascimento"], info["nacionalidade"])
        if not self.verificarSeHaMembroDuplicado(novoMembro):
            self.membrosAcademia.append(novoMembro)
            self.controladorSistema.adicionarPessoa(novoMembro)
            self.telaMembroAcademia.mostraMensagem(f"\n✅ Membro '{novoMembro.nome}' cadastrado com ID {novoMembro.id}!")
        else:
            self.telaMembroAcademia.mostraMensagem(f"\n Membro '{novoMembro.nome}' já cadastrado!")

    def delMembro(self):
        self.telaMembroAcademia.mostraMensagem("\n--- Remover Membro ---")
        membroRemovido = self.buscarMembroAcademia()
        self.membrosAcademia.remove(membroRemovido)
        self.telaMembroAcademia.mostraMensagem(f"\n✅ Membro '{membroRemovido.nome}' foi removdo com sucesso!")        

    def listarMembros(self):
        self.telaMembroAcademia.listarMembros(self.membrosAcademia)
        

    def verificarSeHaMembroDuplicado(self, copia: MembroAcademia):
        for membro in self.membrosAcademia:
            if membro.nome == copia.nome:
                return True
        return False
            
    def buscarMembroAcademia(self):
        while True:
            id = self.telaMembroAcademia.buscarMembroAcademiaInfo()
            for membro in self.membrosAcademia:
                if membro.id == id:
                    return membro
            print("Membro não encontrado! Tente novamente.")

    # Terminar
    def indicar(self):
        self.telaMembroAcademia.mostraMensagem(" --- Votar ---")
        membro = self.buscarMembroAcademia()
        while True:
            categoria = self.telaMembroAcademia.getInt("Id da Categoria: ")
            if categoria in membro.categoriasIndicacao:
                break
            print(f"{membro.nome} não pode votar nessa categoria!")
            