from Entidades.Indicacao import Indicacao
from Limite.TelaIndicacao import TelaIndicacao

class ControladorIndicacao:
    def __init__(self, controladorSistema):
        self.__indicacoes = []
        self.__controladorSistema = controladorSistema
        self.__telaIndicacao = TelaIndicacao(self)

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
            opcao = self.telaIndicacao.exibirMenu()
            if opcao == 0:
                break
            funcao = listaFuncoes.get(opcao)
            if funcao:
                funcao()
            else:
                self.telaIndicacao.mostraMensagem("Opção inválida!")

    def addIndicacao(self):
        self.telaIndicacao.mostraMensagem("\n--- Adicionar Indicação ---")

        categorias = self.controladorSistema.controladorCategorias.categorias
        if not categorias:
            self.telaIndicacao.mostraMensagem("Nenhuma categoria cadastrada!")
            return
        for i, cat in enumerate(categorias, 1):
            self.telaIndicacao.mostraMensagem(f"{i} - {cat.nome}")
        idx_cat = self.telaIndicacao.getInt("Escolha a categoria (número): ") - 1
        if idx_cat < 0 or idx_cat >= len(categorias):
            self.telaIndicacao.mostraMensagem("Categoria inválida.")
            return
        categoria = categorias[idx_cat]

        membros = self.controladorSistema.controladorMembroAcademia.membrosAcademia
        if not membros:
            self.telaIndicacao.mostraMensagem("Nenhum membro da academia cadastrado!")
            return
        for i, membro in enumerate(membros, 1):
            self.telaIndicacao.mostraMensagem(f"{i} - {membro.nome} (ID: {membro.id})")
        idx_membro = self.telaIndicacao.getInt("Escolha o membro que está indicando (número): ") - 1
        if idx_membro < 0 or idx_membro >= len(membros):
            self.telaIndicacao.mostraMensagem("Membro inválido.")
            return
        membro = membros[idx_membro]

        if categoria.e_filme:
            filmes = self.controladorSistema.controladorFilmes.filmes
            if not filmes:
                self.telaIndicacao.mostraMensagem("Nenhum filme cadastrado!")
                return
            for i, filme in enumerate(filmes, 1):
                self.telaIndicacao.mostraMensagem(f"{i} - {filme.titulo} ({filme.ano})")
            idx_filme = self.telaIndicacao.getInt("Escolha o filme indicado (número): ") - 1
            if idx_filme < 0 or idx_filme >= len(filmes):
                self.telaIndicacao.mostraMensagem("Filme inválido.")
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
                self.telaIndicacao.mostraMensagem("Nenhum participante cadastrado para essa função!")
                return
            for i, part in enumerate(participantes_filtrados, 1):
                self.telaIndicacao.mostraMensagem(f"{i} - {part.participante.nome} ({part.funcao.nome} em '{part.filme.titulo}')")
            idx_part = self.telaIndicacao.getInt("Escolha o participante indicado (número): ") - 1
            if idx_part < 0 or idx_part >= len(participantes_filtrados):
                self.telaIndicacao.mostraMensagem("Participante inválido.")
                return
            indicado = participantes_filtrados[idx_part]

        nova_indicacao = Indicacao(indicado, categoria, membro)
        self.indicacoes.append(nova_indicacao)
        self.telaIndicacao.mostraMensagem("\n✅ Indicação cadastrada com sucesso!")


    def delIndicacao(self):
        self.telaIndicacao.mostraMensagem("\n--- Remover Indicação ---")
        if not self.indicacoes:
            self.telaIndicacao.mostraMensagem("Nenhuma indicação cadastrada!")
            return
        for i, ind in enumerate(self.indicacoes, 1):
            self.telaIndicacao.mostraMensagem(f"{i} - {self._descricao_indicacao(ind)}")
        idx = self.telaIndicacao.getInt("Escolha a indicação para remover (número): ") - 1
        if idx < 0 or idx >= len(self.indicacoes):
            self.telaIndicacao.mostraMensagem("Índice inválido.")
            return
        removida = self.indicacoes.pop(idx)
        self.telaIndicacao.mostraMensagem(f"\n✅ Indicação removida: {self._descricao_indicacao(removida)}")

    def listarIndicacoes(self):
        self.telaIndicacao.mostraMensagem("\n--- Lista de Indicações ---")
        if not self.indicacoes:
            self.telaIndicacao.mostraMensagem("Nenhuma indicação cadastrada!")
            return
        for i, ind in enumerate(self.indicacoes, 1):
            self.telaIndicacao.mostraMensagem(f"{i} - {self._descricao_indicacao(ind)}")
        input()

    def detalharIndicacao(self):
        self.telaIndicacao.mostraMensagem("\n--- Detalhar Indicação ---")
        if not self.indicacoes:
            self.telaIndicacao.mostraMensagem("Nenhuma indicação cadastrada!")
            return
        for i, ind in enumerate(self.indicacoes, 1):
            self.telaIndicacao.mostraMensagem(f"{i} - {self._descricao_indicacao(ind)}")
        idx = self.telaIndicacao.getInt("Escolha a indicação para detalhar (número): ") - 1
        if idx < 0 or idx >= len(self.indicacoes):
            self.telaIndicacao.mostraMensagem("Índice inválido.")
            return
        ind = self.indicacoes[idx]
        self.telaIndicacao.mostraMensagem("Detalhes da Indicação:")
        self.telaIndicacao.mostraMensagem(f"Categoria: {ind.categoria.nome}")
        if ind.categoria.e_filme:
            self.telaIndicacao.mostraMensagem(f"Filme: {ind.indicado.titulo} ({ind.indicado.ano})")
        else:
            self.telaIndicacao.mostraMensagem(f"Participante: {ind.indicado.participante.nome} ({ind.indicado.funcao.nome} em '{ind.indicado.filme.titulo}')")
        self.telaIndicacao.mostraMensagem(f"Indicado por: {ind.membro.nome}")
        input()

    def _descricao_indicacao(self, ind):
        if ind.categoria.e_filme:
            return f"[{ind.categoria.nome}] Filme: {ind.indicado.titulo} ({ind.indicado.ano}) | Membro: {ind.membro.nome}"
        else:
            return f"[{ind.categoria.nome}] Participante: {ind.indicado.participante.nome} ({ind.indicado.funcao.nome} em '{ind.indicado.filme.titulo}') | Membro: {ind.membro.nome}"
