from Entidades.Participante import Participante
from Entidades.Pessoa import Pessoa
from Entidades.Filme import Filme
from Entidades.Funcao import Funcao
from Limite.TelaPessoas import TelaPessoas
from datetime import date

class ControladorParticipante:
    def __init__(self, controladorSistema):
        self.__participantes = []
        self.__controladorSistema = controladorSistema
        self.__telaParticipante = TelaPessoas(self)

        pessoa1 = Pessoa("Leonardo DiCaprio", "Masculino", "Americano", date(1974, 11, 11))
        filme1 = Filme("O Regresso", 2015, "Drama", "Um caçador luta para sobreviver após ser atacado por um urso.")
        funcao1 = Funcao("Ator", "Atuação masculina principal")
        self.__participantes.append(Participante(pessoa1, filme1, funcao1))

        pessoa2 = Pessoa("Emma Stone", "Feminino", "Americana", date(1988, 11, 6))
        filme2 = Filme("La La Land", 2016, "Musical", "Um pianista de jazz e uma atriz se apaixonam em Los Angeles.")
        funcao2 = Funcao("Atriz", "Atuação feminina principal")
        self.__participantes.append(Participante(pessoa2, filme2, funcao2))

        pessoa3 = Pessoa("Alejandro González Iñárritu", "Masculino", "Mexicano", date(1963, 8, 15))
        filme3 = Filme("O Regresso", 2015, "Drama", "Um caçador luta para sobreviver após ser atacado por um urso.")
        funcao3 = Funcao("Diretor", "Direção do filme")
        self.__participantes.append(Participante(pessoa3, filme3, funcao3))

        # Ator Coadjuvante 1
        pessoa_ac1 = Pessoa("Mark Rylance", "Masculino", "Britânico", date(1960, 1, 18))
        filme_ac1 = Filme("Ponte dos Espiões", 2015, "Drama", "Durante a Guerra Fria, um advogado negocia a troca de espiões.")
        funcao_ac1 = Funcao("Ator Coadjuvante", "Atuação masculina coadjuvante")
        self.__participantes.append(Participante(pessoa_ac1, filme_ac1, funcao_ac1))

        # Ator Coadjuvante 2
        pessoa_ac2 = Pessoa("Sylvester Stallone", "Masculino", "Americano", date(1946, 7, 6))
        filme_ac2 = Filme("Creed: Nascido para Lutar", 2015, "Drama", "Rocky Balboa treina o filho de Apollo Creed.")
        funcao_ac2 = Funcao("Ator Coadjuvante", "Atuação masculina coadjuvante")
        self.__participantes.append(Participante(pessoa_ac2, filme_ac2, funcao_ac2))

        # Atriz Coadjuvante 1
        pessoa_fem1 = Pessoa("Alicia Vikander", "Feminino", "Sueca", date(1988, 10, 3))
        filme_fem1 = Filme("A Garota Dinamarquesa", 2015, "Drama", "A história da primeira transgênero a realizar uma cirurgia de redesignação sexual.")
        funcao_fem1 = Funcao("Atriz Coadjuvante", "Atuação feminina coadjuvante")
        self.__participantes.append(Participante(pessoa_fem1, filme_fem1, funcao_fem1))

        # Atriz Coadjuvante 2
        pessoa_fem2 = Pessoa("Kate Winslet", "Feminino", "Britânica", date(1975, 10, 5))
        filme_fem2 = Filme("Steve Jobs", 2015, "Drama", "A vida do fundador da Apple em três atos.")
        funcao_fem2 = Funcao("Atriz Coadjuvante", "Atuação feminina coadjuvante")
        self.__participantes.append(Participante(pessoa_fem2, filme_fem2, funcao_fem2))

    @property
    def participantes(self):
        return self.__participantes

    @property
    def controladorSistema(self):
        return self.__controladorSistema

    @property
    def telaParticipante(self):
        return self.__telaParticipante

    def exibirMenu(self):
        listaFuncoes = {
            1: self.addParticipante,
            2: self.delParticipante,
            3: self.listarParticipantes,
            4: self.detalharParticipante
        }
        while True:
            opcao = self.telaParticipante.exibirMenu()
            if opcao == 0:
                break
            funcao = listaFuncoes.get(opcao)
            if funcao:
                funcao()
            else:
                self.telaParticipante.mostraMensagem("Opção inválida!")

    def addParticipante(self):
        info = self.telaParticipante.addPessoaInfo()
        nome_filme = self.telaParticipante.getString("Nome do Filme: ")
        ano_filme = self.telaParticipante.getInt("Ano do Filme: ")
        genero_filme = self.telaParticipante.getString("Gênero do Filme: ")
        sinopse_filme = self.telaParticipante.getString("Sinopse do Filme: ")
        nome_funcao = self.telaParticipante.getString("Função (ex: Ator, Diretor): ")
        descricao_funcao = self.telaParticipante.getString("Descrição da Função: ")

        pessoa = Pessoa(info["nome"], info["sexo"], info["nacionalidade"], info["nascimento"])
        filme = Filme(nome_filme, ano_filme, genero_filme, sinopse_filme)
        funcao = Funcao(nome_funcao, descricao_funcao)
        novoParticipante = Participante(pessoa, filme, funcao)

        if not self.verificarSeHaParticipanteDuplicado(novoParticipante):
            self.participantes.append(novoParticipante)
            self.telaParticipante.mostraMensagem(f"\n✅ Participante '{pessoa.nome}' cadastrado!")
        else:
            self.telaParticipante.mostraMensagem(f"\n Participante '{pessoa.nome}' já cadastrado!")

    def verificarSeHaParticipanteDuplicado(self, copia: Participante):
        for participante in self.participantes:
            if participante.participante.nome == copia.participante.nome and participante.filme.titulo == copia.filme.titulo:
                return True
        return False

    def delParticipante(self):
        self.telaParticipante.mostraMensagem("\n--- Remover Participante ---")
        participanteRemovido = self.buscarParticipante()
        self.participantes.remove(participanteRemovido)
        self.telaParticipante.mostraMensagem(f"\n✅ Participante '{participanteRemovido.participante.nome}' foi removido com sucesso!")

    def buscarParticipante(self):
        while True:
            nome = self.telaParticipante.getString("Nome do Participante: ")
            for participante in self.participantes:
                if participante.participante.nome == nome:
                    return participante
            self.telaParticipante.mostraMensagem("Participante não encontrado! Tente novamente.")

    def listarParticipantes(self):
        self.telaParticipante.mostraMensagem("\n--- Lista de Participantes ---")
        for participante in self.participantes:
            self.telaParticipante.mostraMensagem(f"{participante.participante.nome} ({participante.funcao.nome} em '{participante.filme.titulo}')")
        input()

    def detalharParticipante(self):
        self.telaParticipante.mostraMensagem("\n--- Detalhar Participante ---")
        participante = self.buscarParticipante()
        self.telaParticipante.mostraMensagem(f"Nome: {participante.participante.nome}")
        self.telaParticipante.mostraMensagem(f"Filme: {participante.filme.titulo}")
        self.telaParticipante.mostraMensagem(f"Função: {participante.funcao.nome}")
        input()
