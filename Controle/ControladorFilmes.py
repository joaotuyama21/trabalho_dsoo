from Entidades.Filme import Filme
from Limite.TelaFilme import TelaFilme

class ControladorFilmes:
    def __init__(self, controladorSistema):
        self.__filmes = []
        self.__controladorSistema = controladorSistema
        self.__telaFilme = TelaFilme(self)
        self.__filmes.append(Filme("Guerra Mundial I", 2015, "Aventura", "BOOM PÁ PÁ PÁ TRATRATRATRA BOOOM"))
        self.__filmes.append(Filme("O Regresso", 2015, "Drama", "Um caçador luta para sobreviver após ser atacado por um urso."))
        self.__filmes.append(Filme("La La Land", 2016, "Musical", "Um pianista de jazz e uma atriz se apaixonam em Los Angeles."))

    @property
    def filmes(self):
        return self.__filmes

    @property
    def telaFilme(self):
        return self.__telaFilme

    @property
    def controladorSistema(self):
        return self.__controladorSistema

    def exibirMenu(self):
        listaFuncoes = {
            1: self.addFilme,
            2: self.delFilme,
            3: self.listarFilmes,
            4: self.detalharFilme
        }
        while True:
            opcao = self.telaFilme.exibirMenu()
            if opcao == 0:
                break
            funcao = listaFuncoes.get(opcao)
            if funcao:
                funcao()
            else:
                self.telaFilme.mostraMensagem("Opção inválida!")

    def addFilme(self):
        info = self.telaFilme.addFilmeInfo()
        novoFilme = Filme(info["titulo"], info["ano"], info["genero"], info["sinopse"])
        if not self.verificarSeHaFilmeDuplicado(novoFilme):
            self.filmes.append(novoFilme)
            self.telaFilme.mostraMensagem(f"\n✅ Filme '{novoFilme.titulo}' cadastrado com sucesso!")
        else:
            self.telaFilme.mostraMensagem(f"\nFilme '{novoFilme.titulo}' já cadastrado!")

    def verificarSeHaFilmeDuplicado(self, novoFilme):
        for filme in self.filmes:
            if novoFilme.titulo == filme.titulo:
                return True
        return False

    def delFilme(self):
        self.telaFilme.mostraMensagem("--- Remover Filme ---")
        filmeRemover = self.buscarFilme()
        self.filmes.remove(filmeRemover)
        self.telaFilme.mostraMensagem(f"\n✅ Filme '{filmeRemover.titulo}' removido com sucesso")

    def buscarFilme(self):
        while True:
            nomeFilme = self.telaFilme.getString("Nome do Filme: ")
            for filme in self.filmes:
                if filme.titulo == nomeFilme:
                    return filme
            self.telaFilme.mostraMensagem("Filme não encontrado. Tente Novamente!")

    def listarFilmes(self):
        self.telaFilme.mostraMensagem("\n--- Lista de Filmes ---")
        for i, filme in enumerate(self.filmes, 1):
            self.telaFilme.mostraMensagem(f"{i} - {filme.titulo} ({filme.ano})")
        input()

    def detalharFilme(self):
        self.telaFilme.mostraMensagem("\n--- Detalhar Filme ---")
        filmeDetalhar = self.buscarFilme()
        self.telaFilme.mostraMensagem(f"Ano: {filmeDetalhar.ano}")
        self.telaFilme.mostraMensagem(f"Gênero: {filmeDetalhar.genero}")
        self.telaFilme.mostraMensagem(f"Sinopse: {filmeDetalhar.sinopse}")
        input()
