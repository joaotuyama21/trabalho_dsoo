from Entidades.Participante import Participante
from Entidades.Voto import Voto
from Entidades.Filme import Filme
from Entidades.Indicacao import Indicacao
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
                except (SemCadastrosException, MembroJaVotouNessaCategoriaException, IndiceInvalidoException) as e:
                    self.telaVoto.mostra_mensagem(f'Erro: {e}')
            else:
                self.telaVoto.mostra_mensagem("Opção inválida!")

    def addVoto(self):
        membros = self.controladorSistema.controladorMembroAcademia.membrosAcademia
        if not membros:
            raise SemCadastrosException
        
        categorias = self.controladorSistema.controladorCategorias.categorias
        if not categorias:
            raise SemCadastrosException
        
        # Selecionar o membro
        membroNome = []
        for membro in membros:
            membroNome.append(membro.nome)
        button, idx_membro = self.telaVoto.selecionar(membroNome)
        if button in (None, 'Cancelar'):
            return None
        if idx_membro < 0 or idx_membro >= len(membros):
            raise IndiceInvalidoException
        membro = membros[idx_membro]

        # Seleciona a categoria
        categoriasNome = []
        for categoria in categorias:
            categoriasNome.append(categoria.nome)
        button, idx_cat = self.telaVoto.selecionar(categoriasNome)
        if button in (None, 'Cancelar'):
            return None
        if idx_cat < 0 or idx_cat >= len(categorias):
            raise IndiceInvalidoException
        categoria = categorias[idx_cat]

        if categoria.e_filme:
            filmes = self.controladorSistema.controladorFilmes.filmes
            if not filmes:
                self.telaVoto.mostra_mensagem("Nenhum filme cadastrado!")
                raise SemCadastrosException

            nomeFilmes = []
            for filme in filmes:
                nomeFilmes.append(filme.titulo)
            button, idx_indicado = self.telaVoto.selecionar(nomeFilmes)
            if button in (None, 'Cancelar'):
                return None
            if idx_indicado < 0 or idx_indicado >= len(filmes):
                raise IndiceInvalidoException
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

            nomeParticipantes = []
            for participante in participantes_filtrados:
                nomeParticipantes.append(f'{participante.participante.nome} ({participante.funcao.nome} em {participante.filme.titulo})')
            button, idx_indicado = self.telaVoto.selecionar(nomeParticipantes)
            if button in (None, 'Cancelar'):
                return None
            if idx_indicado < 0 or idx_indicado >= len(participantes_filtrados):
                raise IndiceInvalidoException
            indicado = participantes_filtrados[idx_indicado]

        for voto in self.votos:
            if voto.membro == membro and voto.categoria == categoria:
                raise MembroJaVotouNessaCategoriaException

        novo_voto = Voto(membro, categoria, indicado)
        self.votos.append(novo_voto)
        self.telaVoto.mostra_mensagem("✅ Voto registrado com sucesso!")


    def delVoto(self):
        if not self.votos:
            raise SemCadastrosException
        
        nomeVotos = []
        for voto in self.votos:
            if isinstance(voto.indicado, Filme):
                indicado = voto.indicado.titulo
            else:
                indicado = voto.indicado.participante.nome
            nomeVotos.append(f'{indicado} indicado por {voto.membro.nome}')
        button, idx = self.telaVoto.selecionar(nomeVotos)
        if button in ('Cancelar', None):
            return None
        if idx < 0 or idx >= len(self.votos):
            raise IndiceInvalidoException
        removido = self.votos.pop(idx)
        self.telaVoto.mostra_mensagem("✅ Voto removido com sucesso!")

    def listarVotos(self):
        if not self.votos:
            raise SemCadastrosException
        votosDetalhes = []
        for voto in self.votos:
            if isinstance(voto.indicado, Filme):
                votosDetalhes.append({
                    'Nome': voto.indicado.titulo,
                    'Categoria': voto.categoria.nome,
                    'Membro': voto.membro.nome
                })
            else: 
                votosDetalhes.append({
                    'Nome': voto.indicado.participante.nome,
                    'Categoria': voto.categoria.nome,
                    'Membro': voto.membro.nome
                })
        self.telaVoto.listarVotos(votosDetalhes)


    def detalharVoto(self):
        self.telaVoto.mostra_mensagem("\n--- Detalhar Voto ---")
        if not self.votos:
            self.telaVoto.mostra_mensagem("Nenhum voto registrado!")
            return
        for i, voto in enumerate(self.votos, 1):
            self.telaVoto.mostra_mensagem(f"{i} - {self._descricao_voto(voto)}")
        idx = self.telaVoto.getInt("Escolha o voto para detalhar (número): ") - 1
        if idx < 0 or idx >= len(self.votos):
            raise IndiceInvalidoException
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
                ordenados = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
                vencedor = ordenados[0]
                lugar2 = ordenados[1] if len(ordenados) > 1 else None
                lugar3 = ordenados[2] if len(ordenados) > 2 else None

                resultados[categoria.nome] = {
                    '1° Lugar': vencedor[0],
                    'votos': vencedor[1],
                    '2° Lugar': lugar2[0] if lugar2 else None,
                    'votos_2': lugar2[1] if lugar2 else 0,
                    '3° Lugar': lugar3[0] if lugar3 else None,
                    'votos_3': lugar3[1] if lugar3 else 0,
                    'total_votos': len(votos_categoria)
                }
        return resultados