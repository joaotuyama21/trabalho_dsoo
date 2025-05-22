from Entidades.Filme import Filme
from Limite.TelaFilme import TelaFilme

class ControladorFilmes:
    def __init__(self, controladorSistema):
        self.__filmes = []
        self.__controladorSistema = controladorSistema
        self.__telaFilme = TelaFilme(self)

        self.filmes.append(Filme("Guerra Mundial I", 2015, "Aventura", "BOOM PÁ PÁ PÁ TRATRATRATRA BOOOM"))

    @property
    def filmes(self):
        return self.__filmes

    @property
    def telaFilme(self):
        return self.__telaFilme

    def exibirMenu(self):
        listaFuncoes = {1: self.addFilme, 2: self.delFilme, 3: self.listarFilmes, 4: self.detalharFilme}

        while True:
            opcao = self.telaFilme.exibirMenu()
            if opcao == 0:
                break
            funcao = listaFuncoes[opcao]
            funcao()

    def addFilme(self):
        info = self.telaFilme.addFilmeInfo()
        novoFilme = Filme(info["titulo"], info["ano"], info["genero"], info["sinopse"])
        if not self.verificarSeHaFilmeDuplicado(novoFilme):
            self.filmes.append(novoFilme)
            self.telaFilme.mostraMensagem(f"\n✅ Filme '{novoFilme.titulo}' cadastrado com sucesso!")
        else:
            self.telaFilme.mostraMensagem(f"\n Filme '{novoFilme.titulo}' já cadastrado!")

    def verificarSeHaFilmeDuplicado(self, novoFilme):
        for filme in self.filmes:
            if novoFilme.titulo == filme.titulo:
                return True
        return False

    def delFilme(self):
        self.telaFilme.mostraMensagem("--- Remover Filme ---")
        filmeRemover = self.buscarFilme()
        self.filmes.remove(filmeRemover)
        self.telaFilme.mostraMensagem(f"\n ✅ Filme '{filmeRemover.titulo}' removido com sucesso")


    def buscarFilme(self):
        while True:
            nomeFilme = self.telaFilme.getString("Nome do Filme: ")
            for filme in self.filmes:
                if filme.titulo == nomeFilme:
                    return filme
            self.telaFilme.mostraMensagem("Filme não encontrado. Tente Novamente!")

    def listarFilmes(self):
        self.telaFilme.mostraMensagem("\n--- Lista de Filmes ---")
        filmes = self.filmes
        for i in range(len(filmes)):
            self.telaFilme.mostraMensagem(f"{i+1} - {filmes[i].titulo} ({filmes[i].ano})")
        input()

    def detalharFilme(self):
        self.telaFilme.mostraMensagem("\n--- Detalhar Filme ---")
        filmeDetalhar = self.buscarFilme()
        self.telaFilme.mostraMensagem(f"Ano: {filmeDetalhar.ano}")
        self.telaFilme.mostraMensagem(f"Genero: {filmeDetalhar.genero}")
        self.telaFilme.mostraMensagem(f"Sinopse: {filmeDetalhar.sinopse}")
        input()