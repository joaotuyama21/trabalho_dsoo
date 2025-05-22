from Entidades.Categoria import Categoria
from Limite.TelaCategoria import TelaCategoria

class ControladorCategoria:
    def __init__(self, controladorSistema):
        self.__categorias = []
        self.__telaCategoria = TelaCategoria(self)
        self.__controladorSistema = controladorSistema

    @property
    def categorias(self) -> list:
        return self.__categorias
    
    @property
    def telaCategoria(self) -> TelaCategoria:
        return self.__telaCategoria
    
    @property
    def controladorSistema(self):
        return self.__controladorSistema

    def exibirMenu(self):
        listaFuncoes = {1: self.addCategoria, 2: self.delCategoria, 3: self.listarCategorias, 4: self.detalharCategoria}

        while True:
            opcao = self.telaCategoria.exibirMenu()
            if opcao == 0:
                break
            funcao = listaFuncoes[opcao]
            funcao()

    def addCategoria(self):
        info = self.telaCategoria.addCategoriaInfo()
        novaCategoria = Categoria(info["nome"], info["funcao"])
        if not self.verificarSeHaCategoriaDuplicado(novaCategoria):
            self.categorias.append(novaCategoria)
            self.telaCategoria.mostraMensagem(f"\n✅ Categoria '{novaCategoria.nome}' cadastrada com sucesso!")
        else:
            self.telaCategoria.mostraMensagem(f"\n Categoria '{novaCategoria.nome}' já cadastrada!")

    def verificarSeHaCategoriaDuplicado(self, novaCategoria):
        for categoria in self.categorias:
            if novaCategoria.nome == categoria.nome:
                return True
        return False

    def delCategoria(self):
        self.telaCategoria.mostraMensagem("\n--- Remover Categoria ---")
        categoriaRemover = self.buscarCategoria()
        self.categorias.remove(categoriaRemover)
        self.telaCategoria.mostraMensagem(f"\n ✅ Categoria '{categoriaRemover.nome}' removida com sucesso")


    def buscarCategoria(self):
        while True:
            nomeCategoria = self.telaCategoria.getString("Nome da Categoria: ")
            for categoria in self.categorias:
                if categoria.nome == nomeCategoria:
                    return categoria
            self.telaCategoria.mostraMensagem("Categoria não encontrada. Tente Novamente!")

    def listarCategorias(self):
        self.telaCategoria.mostraMensagem("\n--- Lista de Categorias ---")
        categorias = self.categorias
        for i in range(len(categorias)):
            self.telaCategoria.mostraMensagem(f"{i+1} - {categorias[i].nome}")
        input()

    def detalharCategoria(self):
        self.telaCategoria.mostraMensagem("\n--- Detalhar Categoria ---")
        categoriaDetalhar = self.buscarCategoria()
        self.telaCategoria.mostraMensagem(f"Função: {categoriaDetalhar.funcao}")
        input()