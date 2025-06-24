from Entidades.MembroAcademia import MembroAcademia
from Limite.TelaMembroAcademia import TelaMembroAcademia
from Entidades.Indicacao import Indicacao
from datetime import date

class ControladorMembroAcademia:
    def __init__(self, controladorSistema):
        self.__membrosAcademia = []
        self.__controladorSistema = controladorSistema
        self.__telaMembroAcademia = TelaMembroAcademia(self)
        
        self.__membrosAcademia.append(MembroAcademia("Fernanda Montenegro", "Feminino", date(1929, 10, 16), "Brasileira"))
        self.__membrosAcademia.append(MembroAcademia("Steven Spielberg", "Masculino", date(1946, 12, 18), "Americano"))
        self.__membrosAcademia.append(MembroAcademia("Pedro Almodóvar", "Masculino", date(1949, 9, 25), "Espanhol"))

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
        lista_opcoes = {
            1: self.addMembro,
            2: self.delMembro,
            3: self.listarMembros,
            4: self.indicar
        }
        while True:
            opcao = self.telaMembroAcademia.exibirMenuMembros()
            if opcao == 0:
                break
            funcao = lista_opcoes.get(opcao)
            if funcao:
                funcao()
            else:
                self.telaMembroAcademia.mostra_mensagem("Opção inválida!")

    def addMembro(self):
        button, info = self.telaMembroAcademia.incluirMembroInfo()
        sexo = 'Masculino' if info['M'] else 'F'
        if button == 'Cancelar':
            return None
        if info['nascimento'] is None or info['nascimento'] == '':
            self.telaMembroAcademia.mostra_mensagem("Tá de palhaçada, meu parceiro?")
            return None
        data = info['nascimento'].split('/')
        info['nascimento'] = date(int(data[2]), int(data[1]), int(data[0]))
        novoMembro = MembroAcademia(info["nome"], sexo, info["nascimento"], info["nacionalidade"])
        if not self.verificarSeHaMembroDuplicado(novoMembro):
            self.membrosAcademia.append(novoMembro)
            self.controladorSistema.adicionarPessoa(novoMembro)
            self.telaMembroAcademia.mostra_mensagem(f"\n✅ Membro '{novoMembro.nome}' cadastrado com ID {novoMembro.id}!")
        else:
            self.telaMembroAcademia.mostra_mensagem(f"\nMembro '{novoMembro.nome}' já cadastrado!")

    def verificarSeHaMembroDuplicado(self, novoMembro):
        for membro in self.membrosAcademia:
            if membro.nome == novoMembro.nome:
                return True
        return False

    def delMembro(self):
        button, membroRemover = self.buscarMembro()
        if button == 'Confirmar':
            self.membrosAcademia.remove(membroRemover)
            self.telaMembroAcademia.mostra_mensagem(f"\n✅ Membro '{membroRemover.nome}' removido com sucesso")

    def buscarMembro(self):
        button, values = self.telaMembroAcademia.buscarMembroAcademiaInfo()
        nomeMembro = values['nome']
        if button == 'Confirmar':
            for membro in self.membrosAcademia:
                if membro.nome == nomeMembro:
                    return button,membro
            self.telaMembroAcademia.mostra_mensagem("Membro não encontrado. Tente Novamente!")
        return button, None

    def listarMembros(self):
        self.telaMembroAcademia.listarMembros(self.membrosAcademia)

    def indicar(self):
        self.telaMembroAcademia.mostraMensagem("\n--- Indicar Filme ou Participante ---")
        membro = self.buscarMembro()
        categorias = self.controladorSistema.controladorCategorias.categorias
        if not categorias:
            self.telaMembroAcademia.mostraMensagem("Nenhuma categoria cadastrada!")
            return
        for i, cat in enumerate(categorias, 1):
            self.telaMembroAcademia.mostraMensagem(f"{i} - {cat.nome}")
        idx_cat = self.telaMembroAcademia.getInt("Escolha a categoria (número): ") - 1
        if idx_cat < 0 or idx_cat >= len(categorias):
            self.telaMembroAcademia.mostraMensagem("Categoria inválida.")
            return
        categoria = categorias[idx_cat]

        if categoria.e_filme:
            filmes = self.controladorSistema.controladorFilmes.filmes
            if not filmes:
                self.telaMembroAcademia.mostraMensagem("Nenhum filme cadastrado!")
                return
            for i, filme in enumerate(filmes, 1):
                self.telaMembroAcademia.mostraMensagem(f"{i} - {filme.titulo} ({filme.ano})")
            idx_filme = self.telaMembroAcademia.getInt("Escolha o filme indicado (número): ") - 1
            if idx_filme < 0 or idx_filme >= len(filmes):
                self.telaMembroAcademia.mostraMensagem("Filme inválido.")
                return
            indicado = filmes[idx_filme]
        else:
            participantes = self.controladorSistema.controladorParticipante.participantes
            if not participantes:
                self.telaMembroAcademia.mostraMensagem("Nenhum participante cadastrado!")
                return
            for i, part in enumerate(participantes, 1):
                self.telaMembroAcademia.mostraMensagem(f"{i} - {part.participante.nome} ({part.funcao.nome} em '{part.filme.titulo}')")
            idx_part = self.telaMembroAcademia.getInt("Escolha o participante indicado (número): ") - 1
            if idx_part < 0 or idx_part >= len(participantes):
                self.telaMembroAcademia.mostraMensagem("Participante inválido.")
                return
            indicado = participantes[idx_part]

        nova_indicacao = Indicacao(indicado, categoria, membro)
        self.controladorSistema.controladorIndicacao.indicacoes.append(nova_indicacao)
        self.telaMembroAcademia.mostraMensagem("\n✅ Indicação cadastrada com sucesso!")
