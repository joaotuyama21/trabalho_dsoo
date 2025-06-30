from Entidades.Participante import Participante
from Entidades.Pessoa import Pessoa
from Entidades.Filme import Filme
from Entidades.Funcao import Funcao
from Limite.TelaParticipante import TelaParticipante
from datetime import date
from Exceptions.Excecoes import InstaciaJaCadastradaException, SemCadastrosException
from persistencia import salvar, carregar

class ControladorParticipante:
    def __init__(self, controladorSistema):
        self.__controladorSistema = controladorSistema
        self.__telaParticipante = TelaParticipante(self)
        self.__participantes = carregar('participantes.pkl')
        if not self.__participantes:
            pessoa1 = Pessoa("Leonardo DiCaprio", "Masculino", "Americano", date(1974, 11, 11))
            filme1 = Filme("O Regresso", 2015, "Drama", "Um caçador luta para sobreviver após ser atacado por um urso.")
            funcao1 = Funcao("Ator", "Atuação masculina principal")
            self.__participantes = [
                Participante(pessoa1, filme1, funcao1),
                Participante(
                    Pessoa("Emma Stone", "Feminino", "Americana", date(1988, 11, 6)),
                    Filme("La La Land", 2016, "Musical", "Um pianista de jazz e uma atriz se apaixonam em Los Angeles."),
                    Funcao("Atriz", "Atuação feminina principal")
                ),
                Participante(
                    Pessoa("Alejandro González Iñárritu", "Masculino", "Mexicano", date(1963, 8, 15)),
                    Filme("O Regresso", 2015, "Drama", "Um caçador luta para sobreviver após ser atacado por um urso."),
                    Funcao("Diretor", "Direção do filme")
                ),
                Participante(
                    Pessoa("Mark Rylance", "Masculino", "Britânico", date(1960, 1, 18)),
                    Filme("Ponte dos Espiões", 2015, "Drama", "Durante a Guerra Fria, um advogado negocia a troca de espiões."),
                    Funcao("Ator Coadjuvante", "Atuação masculina coadjuvante")
                ),
                Participante(
                    Pessoa("Sylvester Stallone", "Masculino", "Americano", date(1946, 7, 6)),
                    Filme("Creed: Nascido para Lutar", 2015, "Drama", "Rocky Balboa treina o filho de Apollo Creed."),
                    Funcao("Ator Coadjuvante", "Atuação masculina coadjuvante")
                ),
                Participante(
                    Pessoa("Alicia Vikander", "Feminino", "Sueca", date(1988, 10, 3)),
                    Filme("A Garota Dinamarquesa", 2015, "Drama", "A história da primeira transgênero a realizar uma cirurgia de redesignação sexual."),
                    Funcao("Atriz Coadjuvante", "Atuação feminina coadjuvante")
                ),
                Participante(
                    Pessoa("Kate Winslet", "Feminino", "Britânica", date(1975, 10, 5)),
                    Filme("Steve Jobs", 2015, "Drama", "A vida do fundador da Apple em três atos."),
                    Funcao("Atriz Coadjuvante", "Atuação feminina coadjuvante")
                ),
            ]
            salvar(self.__participantes, 'participantes.pkl')

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
                    self.telaParticipante.mostra_mensagem(f'Erro: {e}')
            else:
                self.telaParticipante.mostra_mensagem("Opção inválida!")

    def addParticipante(self):
        pessoas = self.controladorSistema.controladorPessoas.pessoas
        if not pessoas:
            self.telaParticipante.mostra_mensagem("Nenhuma pessoa cadastrada!")
            return
        nomePessoa = [pessoa.nome for pessoa in pessoas]
        button, id_pessoa = self.telaParticipante.selecionar(nomePessoa)
        if button in (None, 'Cancelar'):
            return
        pessoa = pessoas[id_pessoa]

        filmes = self.controladorSistema.controladorFilmes.filmes
        if not filmes:
            self.telaParticipante.mostra_mensagem("Nenhum filme cadastrado!")
            return
        nomeFilme = [filme.titulo for filme in filmes]
        button, id_filme = self.telaParticipante.selecionar(nomeFilme)
        if button in (None, 'Cancelar'):
            return
        filme = filmes[id_filme]

        button, info = self.telaParticipante.addFuncaoInfo()
        if button in (None, 'Cancelar'):
            return

        funcao = Funcao(info['nome'], info['descricao'])
        novoParticipante = Participante(pessoa, filme, funcao)

        if not self.verificarSeHaParticipanteDuplicado(novoParticipante):
            self.participantes.append(novoParticipante)
            salvar(self.__participantes, 'participantes.pkl')
            self.telaParticipante.mostra_mensagem(f"\n✅ Participante '{pessoa.nome}' cadastrado!")
        else:
            raise InstaciaJaCadastradaException

    def verificarSeHaParticipanteDuplicado(self, copia: Participante):
        for participante in self.participantes:
            if (participante.participante.nome == copia.participante.nome and
                participante.filme.titulo == copia.filme.titulo and
                participante.funcao.nome == copia.funcao.nome):
                return True
        return False

    def delParticipante(self):
        if not self.participantes:
            self.telaParticipante.mostra_mensagem("Nenhum participante para remover!")
            return
        nomeParticipantes = [
            f'{p.participante.nome} como {p.funcao.nome} em {p.filme.titulo}'
            for p in self.participantes
        ]
        button, id_part = self.telaParticipante.selecionar(nomeParticipantes)
        if button in (None, 'Cancelar'):
            return
        participanteRemovido = self.participantes[id_part]
        self.participantes.remove(participanteRemovido)
        salvar(self.__participantes, 'participantes.pkl')
        self.telaParticipante.mostra_mensagem(f"\n✅ Participante '{participanteRemovido.participante.nome}' foi removido com sucesso!")

    def buscarParticipante(self):
        if not self.participantes:
            self.telaParticipante.mostra_mensagem("Nenhum participante cadastrado!")
            return None
        nomeParticipantes = [
            f'{p.participante.nome} como {p.funcao.nome} em {p.filme.titulo}'
            for p in self.participantes
        ]
        button, id_part = self.telaParticipante.selecionar(nomeParticipantes)
        if button in (None, 'Cancelar'):
            return None
        return self.participantes[id_part]

    def listarParticipantes(self):
        if not self.participantes:
            raise SemCadastrosException
        lista = [
            f'{p.participante.nome} como {p.funcao.nome} em {p.filme.titulo}'
            for p in self.participantes
        ]
        self.telaParticipante.listarParticipantes(lista)

    def alterarParticipante(self):
        participanteParaAlterar = self.buscarParticipante()
        if not participanteParaAlterar:
            return

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
            return

        for i in codigoAtr.keys():
            if codigoAtr[i]:
                codigoAtr = int(i)
                break

        if codigoAtr == 1:
            pessoas = self.controladorSistema.controladorPessoas.pessoas
            nomePessoas = [p.nome for p in pessoas]
            button, id_pessoa = self.telaParticipante.selecionar(nomePessoas)
            if button in (None, 'Cancelar'):
                return
            novoValor = pessoas[id_pessoa]
        elif codigoAtr == 2:
            filmes = self.controladorSistema.controladorFilmes.filmes
            nomeFilmes = [f.titulo for f in filmes]
            button, id_filme = self.telaParticipante.selecionar(nomeFilmes)
            if button in (None, 'Cancelar'):
                return
            novoValor = filmes[id_filme]
        elif codigoAtr == 3:
            button, info = self.telaParticipante.addFuncaoInfo()
            if button in (None, 'Cancelar'):
                return
            novoValor = Funcao(info['nome'], info['descricao'])
        else:
            return

        funcao = setters[codigoAtr]
        funcao(novoValor)
        salvar(self.__participantes, 'participantes.pkl')
        self.telaParticipante.mostra_mensagem(f"\n✅ Atributo '{atributos[codigoAtr]}' alterado com sucesso!")

    def detalharParticipante(self):
        participante = self.buscarParticipante()
        if not participante:
            return
        info = {
            'nome': participante.participante.nome,
            'filme': participante.filme.titulo,
            'funcao': participante.funcao.nome
        }
        self.telaParticipante.detalharPessoa(info)
