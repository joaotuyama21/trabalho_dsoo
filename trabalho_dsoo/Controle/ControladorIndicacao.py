from Entidades.Indicacao import Indicacao
from Limite.TelaIndicacao import TelaIndicacao
from persistencia import salvar, carregar

class ControladorIndicacao:
    def __init__(self, controladorSistema):
        self.__controladorSistema = controladorSistema
        self.__telaIndicacao = TelaIndicacao(self)
        self.__indicacoes = carregar('indicacoes.pkl')

    @property
    def indicacoes(self):
        return self.__indicacoes

    @property
    def controladorSistema(self):
        return self.__controladorSistema

    @property
    def telaIndicacao(self):
        return self.__telaIndicacao

    def exibirMenu(self):
        listaFuncoes = {
            1: self.addIndicacao,
            2: self.delIndicacao,
            3: self.listarIndicacoes,
            4: self.detalharIndicacao
        }
        while True:
            button, opcao = self.telaIndicacao.exibirMenu()
            if button in (None, 'Cancelar'):
                return None
            if opcao == 0:
                break
            funcao = listaFuncoes.get(opcao)
            if funcao:
                funcao()
            else:
                self.telaIndicacao.mostra_mensagem("Opção inválida!")

    def addIndicacao(self):
        categorias = self.controladorSistema.controladorCategorias.categorias
        if not categorias:
            self.telaIndicacao.mostra_mensagem("Nenhuma categoria cadastrada! Impossível indicar.")
            return
        membros = self.controladorSistema.controladorMembroAcademia.membrosAcademia
        if not membros:
            self.telaIndicacao.mostra_mensagem("Nenhum membro da academia cadastrado! Impossível indicar.")
            return

        categoriasNome = [categoria.nome for categoria in categorias]
        button, idx_cat = self.telaIndicacao.selecionar(categoriasNome)
        if button in (None, 'Cancelar') or idx_cat < 0 or idx_cat >= len(categorias):
            self.telaIndicacao.mostra_mensagem("Categoria inválida.")
            return
        categoria = categorias[idx_cat]

        membroNome = [membro.nome for membro in membros]
        button, idx_membro = self.telaIndicacao.selecionar(membroNome)
        if button in (None, 'Cancelar') or idx_membro < 0 or idx_membro >= len(membros):
            self.telaIndicacao.mostra_mensagem("Membro inválido.")
            return
        membro = membros[idx_membro]

        if categoria.e_filme:
            filmes = self.controladorSistema.controladorFilmes.filmes
            if not filmes:
                self.telaIndicacao.mostra_mensagem("Nenhum filme cadastrado!")
                return
            nomeFilmes = [filme.titulo for filme in filmes]
            button, idx_filme = self.telaIndicacao.selecionar(nomeFilmes)
            if button in (None, 'Cancelar') or idx_filme < 0 or idx_filme >= len(filmes):
                self.telaIndicacao.mostra_mensagem("Filme inválido.")
                return
            indicado = filmes[idx_filme]
        else:
            participantes = self.controladorSistema.controladorParticipante.participantes
            funcao_categoria = categoria.funcao.nome.strip().lower()
            participantes_filtrados = [
                p for p in participantes
                if p.funcao.nome.strip().lower() == funcao_categoria
            ]
            if not participantes_filtrados:
                self.telaIndicacao.mostra_mensagem("Nenhum participante cadastrado para essa função!")
                return
            nomeParticipantes = [p.participante.nome for p in participantes_filtrados]
            button, idx_part = self.telaIndicacao.selecionar(nomeParticipantes)
            if button in (None, 'Cancelar') or idx_part < 0 or idx_part >= len(participantes_filtrados):
                self.telaIndicacao.mostra_mensagem("Participante inválido.")
                return
            indicado = participantes_filtrados[idx_part]

        nova_indicacao = Indicacao(indicado, categoria, membro)
        self.indicacoes.append(nova_indicacao)
        salvar(self.__indicacoes, 'indicacoes.pkl')
        self.telaIndicacao.mostra_mensagem("\n✅ Indicação cadastrada com sucesso!")

    def delIndicacao(self):
        if not self.indicacoes:
            self.telaIndicacao.mostra_mensagem("Nenhuma indicação cadastrada!")
            return

        indicadoMembro = []
        for indicacao in self.indicacoes:
            if indicacao.categoria.e_filme:
                indicadoMembro.append(f'{indicacao.indicado.titulo} indicado por {indicacao.membroAcademia.nome} como {indicacao.categoria.nome}')
            else:
                indicadoMembro.append(f'{indicacao.indicado.participante.nome} indicado por {indicacao.membroAcademia.nome} como {indicacao.categoria.nome}')
        button, idx = self.telaIndicacao.selecionar(indicadoMembro)
        if button in (None, 'Cancelar') or idx < 0 or idx >= len(self.indicacoes):
            self.telaIndicacao.mostra_mensagem("Índice inválido.")
            return
        self.indicacoes.pop(idx)
        salvar(self.__indicacoes, 'indicacoes.pkl')
        self.telaIndicacao.mostra_mensagem(f"\n✅ Indicação removida")

    def listarIndicacoes(self):
        if not self.indicacoes:
            self.telaIndicacao.mostra_mensagem("Nenhuma indicação cadastrada!")
            return

        indicacaoDetalhes = []
        for indicacao in self.indicacoes:
            indicacaoDetalhes.append(self._descricao_indicacao(indicacao))
        self.telaIndicacao.listarIndicacoes(indicacaoDetalhes)

    def detalharIndicacao(self):
        self.telaIndicacao.mostra_mensagem("\n--- Detalhar Indicação ---")
        if not self.indicacoes:
            self.telaIndicacao.mostra_mensagem("Nenhuma indicação cadastrada!")
            return
        for i, ind in enumerate(self.indicacoes, 1):
            self.telaIndicacao.mostra_mensagem(f"{i} - {self._descricao_indicacao(ind)}")
        idx = self.telaIndicacao.getInt("Escolha a indicação para detalhar (número): ") - 1
        if idx < 0 or idx >= len(self.indicacoes):
            self.telaIndicacao.mostra_mensagem("Índice inválido.")
            return
        ind = self.indicacoes[idx]
        self.telaIndicacao.mostra_mensagem("Detalhes da Indicação:")
        self.telaIndicacao.mostra_mensagem(f"Categoria: {ind.categoria.nome}")
        if ind.categoria.e_filme:
            self.telaIndicacao.mostra_mensagem(f"Filme: {ind.indicado.titulo} ({ind.indicado.ano})")
        else:
            self.telaIndicacao.mostra_mensagem(f"Participante: {ind.indicado.participante.nome} ({ind.indicado.funcao.nome} em '{ind.indicado.filme.titulo}')")
        self.telaIndicacao.mostra_mensagem(f"Indicado por: {ind.membroAcademia.nome}")
        input()

    def _descricao_indicacao(self, ind):
        if ind.categoria.e_filme:
            descricao = {
                'Categoria': f'{ind.categoria.nome}',
                'Filme': f'{ind.indicado.titulo} ({ind.indicado.ano})',
                'Membro': f'{ind.membroAcademia.nome}',
                'eh_filme': True
            }
        else:
            descricao = {
                'Categoria': f"{ind.categoria.nome}",
                "Participante": f'{ind.indicado.participante.nome}',
                'Filme': f'{ind.indicado.filme.titulo}',
                'Membro': f"{ind.membroAcademia.nome}",
                'eh_filme': False
            }
        return descricao
