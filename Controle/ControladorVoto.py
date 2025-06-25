from Entidades import *
from Limite.TelaVoto import TelaVoto
from datetime import date
from Exceptions.Excecoes import *

class ControladorVoto:
    def __init__(self, controladorSistema):
        self.__votos = []
        self.__controladorSistema = controladorSistema
        self.__telaVoto = TelaVoto(self)

    @property
    def votos(self):
        return self.__votos

    @property
    def controladorSistema(self):
        return self.__controladorSistema

    @property
    def telaVoto(self):
        return self.__telaVoto

    def exibirMenu(self):
        listaFuncoes = {
            1: self.addVoto,
            2: self.delVoto,
            3: self.listarVotos,
            4: self.detalharVoto
        }
        while True:
            button, opcao = self.telaVoto.exibirMenu()
            if button in (None, 'Cancelar'):
                break
            funcao = listaFuncoes.get(opcao)
            if funcao:
                try:
                    funcao()
                except (NenhumMembroCadastradoException, NenhumaCategoriaCadastradaException, NenhumFilmeCadastradoException) as e:
                    self.telaVoto.mostra_mensagem(f'Erro: {e}')
            else:
                self.telaVoto.mostra_mensagem("Opção inválida!")

    def addVoto(self):
        membros = self.controladorSistema.controladorMembroAcademia.membrosAcademia
        if not membros:
            raise NenhumMembroCadastradoException
        
        categorias = self.controladorSistema.controladorCategorias.categorias
        if not categorias:
            raise NenhumaCategoriaCadastradaException
        
        # Selecionar o membro
        membroNome = []
        for membro in membros:
            membroNome.append(membro.nome)
        button, idx_membro = self.telaVoto.selecionar(membroNome)
        if button in (None, 'Cancelar'):
            return None
        membro = membros[idx_membro]

        # Seleciona a categoria
        categoriasNome = []
        for categoria in categorias:
            categoriasNome.append(categoria.nome)
        button, idx_cat = self.telaVoto.selecionar(categoriasNome)
        if button in (None, 'Cancelar'):
            return None
        categoria = categorias[idx_cat]

        if categoria.e_filme:
            filmes = self.controladorSistema.controladorFilmes.filmes
            if not filmes:
                self.telaVoto.mostra_mensagem("Nenhum filme cadastrado!")
                raise NenhumFilmeCadastradoException

            nomeFilmes = []
            for filme in filmes:
                nomeFilmes.append(filme.titulo)
            button, idx_indicado = self.telaVoto.selecionar(nomeFilmes)
            if button in (None, 'Cancelar'):
                return None
            indicado = filmes[idx_indicado]
        else:
            # FILTRO ESPECÍFICO POR CATEGORIA
            participantes = self.controladorSistema.controladorParticipante.participantes
            funcao_categoria = categoria.funcao.nome.strip().lower()
            participantes_filtrados = [
                p for p in participantes
                if p.funcao.nome.strip().lower() == funcao_categoria
            ]
            if not participantes_filtrados:
                self.telaVoto.mostra_mensagem("Nenhum participante cadastrado para essa função!")
                return
            for i, part in enumerate(participantes_filtrados, 1):
                self.telaVoto.mostra_mensagem(f"{i} - {part.participante.nome} ({part.funcao.nome} em '{part.filme.titulo}')")
            idx_indicado = self.telaVoto.getInt("Escolha o participante votado (número): ") - 1
            if idx_indicado < 0 or idx_indicado >= len(participantes_filtrados):
                self.telaVoto.mostra_mensagem("Participante inválido.")
                return
            indicado = participantes_filtrados[idx_indicado]

        for voto in self.votos:
            if voto.membro == membro and voto.categoria == categoria:
                self.telaVoto.mostra_mensagem("Este membro já votou nesta categoria!")
                return

        novo_voto = Voto(membro, categoria, indicado)
        self.votos.append(novo_voto)
        self.telaVoto.mostra_mensagem("✅ Voto registrado com sucesso!")


    def delVoto(self):
        self.telaVoto.mostra_mensagem("\n--- Remover Voto ---")
        if not self.votos:
            self.telaVoto.mostra_mensagem("Nenhum voto registrado!")
            return
        for i, voto in enumerate(self.votos, 1):
            self.telaVoto.mostra_mensagem(f"{i} - {self._descricao_voto(voto)}")
        idx = self.telaVoto.getInt("Escolha o voto para remover (número): ") - 1
        if idx < 0 or idx >= len(self.votos):
            self.telaVoto.mostra_mensagem("Índice inválido.")
            return
        removido = self.votos.pop(idx)
        self.telaVoto.mostra_mensagem(f"✅ Voto removido: {self._descricao_voto(removido)}")

    def listarVotos(self):
        self.telaVoto.mostra_mensagem("\n--- Lista de Votos ---")
        if not self.votos:
            self.telaVoto.mostra_mensagem("Nenhum voto registrado!")
            return
        for i, voto in enumerate(self.votos, 1):
            self.telaVoto.mostra_mensagem(f"{i} - {self._descricao_voto(voto)}")
        input()

    def detalharVoto(self):
        self.telaVoto.mostra_mensagem("\n--- Detalhar Voto ---")
        if not self.votos:
            self.telaVoto.mostra_mensagem("Nenhum voto registrado!")
            return
        for i, voto in enumerate(self.votos, 1):
            self.telaVoto.mostra_mensagem(f"{i} - {self._descricao_voto(voto)}")
        idx = self.telaVoto.getInt("Escolha o voto para detalhar (número): ") - 1
        if idx < 0 or idx >= len(self.votos):
            self.telaVoto.mostra_mensagem("Índice inválido.")
            return
        voto = self.votos[idx]
        self.telaVoto.mostra_mensagem("Detalhes do Voto:")
        self.telaVoto.mostra_mensagem(f"Membro: {voto.membro.nome}")
        self.telaVoto.mostra_mensagem(f"Categoria: {voto.categoria.nome}")
        if voto.categoria.e_filme:
            self.telaVoto.mostra_mensagem(f"Filme votado: {voto.indicado.titulo} ({voto.indicado.ano})")
        else:
            self.telaVoto.mostra_mensagem(f"Participante votado: {voto.indicado.participante.nome} ({voto.indicado.funcao.nome} em '{voto.indicado.filme.titulo}')")
        input()

    def _descricao_voto(self, voto):
        if voto.categoria.e_filme:
            return f"[{voto.categoria.nome}] Membro: {voto.membro.nome} | Filme: {voto.indicado.titulo} ({voto.indicado.ano})"
        else:
            return f"[{voto.categoria.nome}] Membro: {voto.membro.nome} | Participante: {voto.indicado.participante.nome} ({voto.indicado.funcao.nome} em '{voto.indicado.filme.titulo}')"

    def calcular_vencedores(self):
        resultados = {}
        for categoria in self.controladorSistema.controladorCategorias.categorias:
            votos_categoria = [v for v in self.votos if v.categoria == categoria]
            contagem = {}

            for voto in votos_categoria:
                chave = voto.indicado.titulo if categoria.e_filme else f"{voto.indicado.participante.nome} ({voto.indicado.funcao.nome})"
                contagem[chave] = contagem.get(chave, 0) + 1

            if contagem:
                vencedor = max(contagem.items(), key=lambda x: x[1])
                resultados[categoria.nome] = {
                    'vencedor': vencedor[0],
                    'votos': vencedor[1],
                    'total_votos': len(votos_categoria)
                }
        return resultados
