from Entidades.Filme import Filme
from Limite.TelaFilme import TelaFilme
from persistencia import salvar, carregar

class ControladorFilmes:
    def __init__(self, controladorSistema):
        self.__controladorSistema = controladorSistema
        self.__telaFilme = TelaFilme(self)
        self.__filmes = carregar('filmes.pkl')
        if not self.__filmes:
            self.__filmes = [
                Filme("Guerra Mundial I", 2015, "Aventura", "BOOM PÁ PÁ PÁ TRATRATRATRA BOOOM"),
                Filme("O Regresso", 2015, "Drama", "Um caçador luta para sobreviver após ser atacado por um urso."),
                Filme("La La Land", 2016, "Musical", "Um pianista de jazz e uma atriz se apaixonam em Los Angeles."),
            ]
            salvar(self.__filmes, 'filmes.pkl')

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
                self.telaFilme.mostra_mensagem("Opção inválida!")

    def addFilme(self):
        button, info = self.telaFilme.addFilmeInfo()
        tipagem = True
        if button in (None, 'Cancelar'):
            return None

        try:
            info['ano'] = int(info['ano'])
        except ValueError:
            self.telaFilme.mostra_mensagem(f"Valor não suportado. Tente Novamente!")
            return None

        novoFilme = Filme(info["titulo"], info["ano"], info["genero"], info["sinopse"])
        if not self.verificarSeHaFilmeDuplicado(novoFilme) and tipagem:
            self.filmes.append(novoFilme)
            salvar(self.__filmes, 'filmes.pkl')
            self.telaFilme.mostra_mensagem(f"\n✅ Filme '{novoFilme.titulo}' cadastrado com sucesso!")
        else:
            self.telaFilme.mostra_mensagem(f"\nFilme '{novoFilme.titulo}' já cadastrado!")

    def verificarSeHaFilmeDuplicado(self, novoFilme):
        for filme in self.filmes:
            if novoFilme.titulo == filme.titulo:
                return True
        return False

    def delFilme(self):
        filmeRemover = self.buscarFilme()
        if filmeRemover is not None:
            self.filmes.remove(filmeRemover)
            salvar(self.__filmes, 'filmes.pkl')
            self.telaFilme.mostra_mensagem(f"\n✅ Filme '{filmeRemover.titulo}' removido com sucesso")

    def buscarFilme(self):
        while True:
            button, nomeFilme = self.telaFilme.buscarFilmeInfo()
            if button in (None, 'Cancelar'):
                break
            for filme in self.filmes:
                if filme.titulo == nomeFilme['titulo']:
                    return filme
            self.telaFilme.mostra_mensagem("Filme não encontrado. Tente Novamente!")

    def listarFilmes(self):
        filmes = []
        for filme in self.filmes:
            filmes.append(filme.titulo)
        self.telaFilme.listarFilmes(filmes)

    def detalharFilme(self):
        filme = self.buscarFilme()
        if filme is not None:
            info = {
                'titulo': filme.titulo,
                'ano': filme.ano,
                'genero': filme.genero,
                'sinopse': filme.sinopse
            }
            self.telaFilme.detalharFilme(info)
