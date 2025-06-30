from Entidades.Participante import Participante
from Entidades.Pessoa import Pessoa
from Entidades.Filme import Filme
from Entidades.Funcao import Funcao
from Limite.TelaParticipante import TelaParticipante
from datetime import date
from Exceptions.Excecoes import InstaciaJaCadastradaException
from Exceptions.Excecoes import SemCadastrosException

class ControladorParticipante:
    def __init__(self, controladorSistema):
        self.__participantes = []
        self.__controladorSistema = controladorSistema
        self.__telaParticipante = TelaParticipante(self)

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
            4: self.detalharParticipante,
            5: self.alterarParticipante
        }
        while True:
            opcao = self.telaParticipante.exibirMenu()
            if opcao == 0:
                break
            funcao = listaFuncoes.get(opcao)
            if funcao:
                try:
                    funcao()
                except (InstaciaJaCadastradaException, SemCadastrosException) as e:
                    print(f'Erro: {e}')
            else:
                self.telaParticipante.mostra_mensagem("Opção inválida!")

    def addParticipante(self):
        pessoas = self.controladorSistema.controladorPessoas.pessoas
        nomePessoa = []
        for pessoa in pessoas:
            nomePessoa.append(pessoa.nome)
        button, id_pessoa = self.telaParticipante.selecionar(nomePessoa)
        if button in (None, 'Cancelar'):
            return
        nomePessoa = pessoas[id_pessoa]

        filmes = self.controladorSistema.controladorFilmes.filmes
        nomeFilme = []
        for filme in filmes:
            nomeFilme.append(filme.titulo)
        button, id_filme = self.telaParticipante.selecionar(nomeFilme)
        if button in (None, 'Cancelar'):
            return
        nomeFilme = filmes[id_pessoa]

        button, info = self.telaParticipante.addFuncaoInfo()
        if button in (None, 'Cancelar'):
            return

        pessoa = Pessoa(nomePessoa.nome, nomePessoa.sexo, nomePessoa.nacionalidade, nomePessoa.nascimento)
        filme = Filme(nomeFilme.titulo, nomeFilme.ano, nomeFilme.genero, nomeFilme.sinopse)
        funcao = Funcao(info['nome'], info['descricao'])
        novoParticipante = Participante(pessoa, filme, funcao)

        if not self.verificarSeHaParticipanteDuplicado(novoParticipante):
            self.participantes.append(novoParticipante)
            self.telaParticipante.mostra_mensagem(f"\n✅ Participante '{pessoa.nome}' cadastrado!")
        else:
            raise InstaciaJaCadastradaException

    def verificarSeHaParticipanteDuplicado(self, copia: Participante):
        for participante in self.participantes:
            if participante.participante.nome == copia.participante.nome and participante.filme.titulo == copia.filme.titulo:
                return True
        return False

    def delParticipante(self):
        participantes = self.participantes
        nomeParticipantes = []
        for participante in participantes:
            nomeParticipantes.append(f'{participante.participante.nome} como {participante.funcao.nome} em {participante.filme.titulo}')
        button, id_part = self.telaParticipante.selecionar(nomeParticipantes)
        if button in (None, 'Cancelar'):
            return
        participanteRemovido = participantes[id_part]
        self.participantes.remove(participanteRemovido)
        self.telaParticipante.mostra_mensagem(f"\n✅ Participante '{participanteRemovido.participante.nome}' foi removido com sucesso!")

    def buscarParticipante(self):
        while True:
            nome = self.telaParticipante.getString("Nome do Participante: ")
            for participante in self.participantes:
                if participante.participante.nome == nome:
                    return participante
            self.telaParticipante.mostra_mensagem("Participante não encontrado! Tente novamente.")

    def listarParticipantes(self):
        if not self.participantes:
            raise SemCadastrosException
        lista = []
        for participante in self.participantes:
            lista.append(f'{participante.participante.nome} como {participante.funcao.nome} em {participante.filme.titulo}')
        self.telaParticipante.listarParticipantes(lista)

    def alterarParticipante(self):
        participantes = self.participantes
        nomeParticipantes = []
        for participante in participantes:
            nomeParticipantes.append(f'{participante.participante.nome} como {participante.funcao.nome} em {participante.filme.titulo}')
        button, id_part = self.telaParticipante.selecionar(nomeParticipantes)
        if button in (None, 'Cancelar'):
            return
        participanteParaAlterar = participantes[id_part]

        setters = {
                   1: participanteParaAlterar.pessoaAlterar,
                   2: participanteParaAlterar.filmeAlterar,
                   3: participanteParaAlterar.funcaoAlterar,
                  }
        atributos = {
                     1: "Pessoa",
                     2: "Filme",
                     3: "Funcao",
                    }
        button, codigoAtr = self.telaParticipante.mostraAtributos(atributos)
        if button in (None, 'Cancelar'):
            return None
        for i in codigoAtr.keys():
            if codigoAtr[i]:
                codigoAtr = int(i)
                break

        if codigoAtr in {1}:
            pessoas = self.controladorSistema.controladorPessoas.pessoas
            nomePessoas = []
            for pessoa in pessoas:
                nomePessoas.append(pessoa.nome)
            button, id_pessoa = self.telaParticipante.selecionar(nomePessoas)
            if button in (None, 'Cancelar'):
                return None
            novoValor = pessoas[id_pessoa]
            self.telaParticipante.mostra_mensagem(f"\n✅ Atributo '{atributos[codigoAtr]}' alterado para '{novoValor.nome}' com sucesso!")
        elif codigoAtr in {2}:
            filmes = self.controladorSistema.controladorFilmes.filmes
            nomeFilme = []
            for filme in filmes:
                nomeFilme.append(filme.titulo)
            button, id_filme = self.telaParticipante.selecionar(nomeFilme)
            if button in (None, 'Cancelar'):
                return None
            novoValor = filmes[id_filme]
            self.telaParticipante.mostra_mensagem(f"\n✅ Atributo '{atributos[codigoAtr]}' alterado para '{novoValor.titulo}' com sucesso!")
        elif codigoAtr in {3}:
            button, info = self.telaParticipante.addFuncaoInfo()
            if button in (None, 'Cancelar'):
                return
            novoValor = Funcao(info['nome'], info['descricao'])
            self.telaParticipante.mostra_mensagem(f"\n✅ Atributo '{atributos[codigoAtr]}' alterado para '{novoValor.nome}' com sucesso!")

        funcao = setters[codigoAtr]
        funcao(novoValor)

    def detalharParticipante(self):
        self.telaParticipante.mostra_mensagem("\n--- Detalhar Participante ---")
        participante = self.buscarParticipante()
        self.telaParticipante.mostra_mensagem(f"Nome: {participante.participante.nome}")
        self.telaParticipante.mostra_mensagem(f"Filme: {participante.filme.titulo}")
        self.telaParticipante.mostra_mensagem(f"Função: {participante.funcao.nome}")
