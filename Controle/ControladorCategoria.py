from Entidades.Categoria import Categoria
from Limite.TelaCategoria import TelaCategoria
from Entidades.Funcao import Funcao

class ControladorCategoria:
    def __init__(self, controladorSistema):
        self.__categorias = []
        self.__telaCategoria = TelaCategoria(self)
        self.__controladorSistema = controladorSistema
        self._cadastrar_categorias_principais()

    def _cadastrar_categorias_principais(self):
        categorias = [
            {"nome": "Melhor Filme", "funcao_nome": "Filme", "funcao_descricao": "Filme principal", "e_filme": True},
            {"nome": "Melhor Direção", "funcao_nome": "Diretor", "funcao_descricao": "Direção do filme", "e_filme": False},
            {"nome": "Melhor Ator", "funcao_nome": "Ator", "funcao_descricao": "Atuação masculina principal", "e_filme": False},
            {"nome": "Melhor Atriz", "funcao_nome": "Atriz", "funcao_descricao": "Atuação feminina principal", "e_filme": False},
            {"nome": "Melhor Ator Coadjuvante", "funcao_nome": "Ator Coadjuvante", "funcao_descricao": "Atuação masculina coadjuvante", "e_filme": False},
            {"nome": "Melhor Atriz Coadjuvante", "funcao_nome": "Atriz Coadjuvante", "funcao_descricao": "Atuação feminina coadjuvante", "e_filme": False},
        ]
        for cat in categorias:
            funcao = Funcao(cat["funcao_nome"], cat["funcao_descricao"])
            categoria = Categoria(cat["nome"], funcao, cat["e_filme"])
            self.__categorias.append(categoria)

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
        listaFuncoes = {
            3: self.listarCategorias,
            4: self.detalharCategoria
        }
        while True:
            opcao = self.telaCategoria.exibirMenu()
            if opcao == 0:
                break
            funcao = listaFuncoes.get(opcao)
            if funcao:
                funcao()
            else:
                self.telaCategoria.mostraMensagem("Opção inválida!")

    def addCategoria(self):
        self.telaCategoria.mostra_mensagem("Cadastro de novas categorias desabilitado. As principais categorias já estão cadastradas.")

    def delCategoria(self):
        self.telaCategoria.mostra_mensagem("Remoção de categorias padrão do Oscar não é permitida.")

    def buscarCategoria(self):
        while True:
            button, nomeCategoria = self.telaCategoria.getString("Nome da Categoria")
            for categoria in self.categorias:
                if categoria.nome == nomeCategoria['key']:
                    return categoria
            self.telaCategoria.mostra_mensagem("Categoria não encontrada. Tente Novamente!")

    def listarCategorias(self):
        nomes = []
        for categoria in self.categorias:
            nomes.append(categoria.nome)
        self.telaCategoria.listarCategorias(nomes)

    def detalharCategoria(self):
        categoriaDetalhar = self.buscarCategoria()
        info = {
            'Nome':categoriaDetalhar.nome,
            'Funcao':categoriaDetalhar.funcao.nome,
            'É filme?':categoriaDetalhar.e_filme
        }
        self.telaCategoria.detalharCategoria(info)
