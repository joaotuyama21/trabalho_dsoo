from Limite.TelaPessoas import TelaPessoas
from Entidades.Pessoa import Pessoa
from datetime import date
from Exceptions.Excecoes import *
from persistencia import salvar, carregar

class ControladorPessoas:
    def __init__(self, controladorSistema):
        self.__controladorSistema = controladorSistema
        self.__telaPessoas = TelaPessoas(self)
        self.__pessoas = carregar('pessoas.pkl')
        if not self.__pessoas:
            self.__pessoas = [
                Pessoa("Leonardo DiCaprio", "Masculino", "Americano", date(1974, 11, 11)),
                Pessoa("Emma Stone", "Feminino", "Americana", date(1988, 11, 6)),
                Pessoa("Alejandro González Iñárritu", "Masculino", "Mexicano", date(1963, 8, 15))
            ]
            salvar(self.__pessoas, 'pessoas.pkl')

    @property
    def pessoas(self):
        return self.__pessoas

    @property
    def controladorSistema(self):
        return self.__controladorSistema

    @property
    def telaPessoas(self):
        return self.__telaPessoas

    def exibirMenu(self):
        listaFuncoes = {
            1: self.addPessoa,
            2: self.delPessoa,
            3: self.listarPessoas,
            4: self.detalharPessoa,
            5: self.alterarPessoa
        }

        while True:
            opcao = self.telaPessoas.exibirMenu()
            if opcao == 0:
                break
            funcao = listaFuncoes.get(opcao)
            if funcao:
                try:
                    funcao()
                except InstaciaJaCadastradaException as e:
                    self.telaPessoas.mostra_mensagem(f'Erro: {e}')
            else:
                self.telaPessoas.mostra_mensagem("Opção inválida!")

    def addPessoa(self):
        button, info = self.telaPessoas.AddPessoaInfo()
        if button in (None, 'Cancelar'):
            return None
        info["sexo"] = 'Masculino' if info['M'] else 'F'
        if info['nascimento'] is None or info['nascimento'] == '':
            self.telaPessoas.mostra_mensagem("Informações incorretas. Tente Novamente!")
            return None
        data = info['nascimento'].split('/')
        info['nascimento'] = date(int(data[2]), int(data[1]), int(data[0]))

        novaPessoa = Pessoa(info["nome"], info["sexo"], info["nacionalidade"], info["nascimento"])
        if not self.verificarSeHaPessoaDuplicado(novaPessoa):
            self.pessoas.append(novaPessoa)
            salvar(self.__pessoas, 'pessoas.pkl')
            self.telaPessoas.mostra_mensagem(f"\n✅ Pessoa '{novaPessoa.nome}' cadastrado com ID {novaPessoa.id}!")
        else:
            raise InstaciaJaCadastradaException

    def verificarSeHaPessoaDuplicado(self, copia: Pessoa) -> bool:
        for pessoa in self.pessoas:
            if pessoa.nome == copia.nome:
                return True
        return False

    def delPessoa(self):
        button, pessoaRemovida = self.buscarPessoa()
        if pessoaRemovida is None:
            return
        try:
            self.pessoas.remove(pessoaRemovida)
            salvar(self.__pessoas, 'pessoas.pkl')
        except ValueError:
            self.telaPessoas.mostra_mensagem(f"\nPessoa '{pessoaRemovida.nome}' não foi removida com sucesso")
        else:
            self.telaPessoas.mostra_mensagem(f"\n✅ Pessoa '{pessoaRemovida.nome}' foi removido com sucesso!")

    def buscarPessoa(self):
        button, values = self.telaPessoas.buscarPessoaInfo()
        nomePessoa = values['nome']
        if button == 'Confirmar':
            for pessoa in self.pessoas:
                if pessoa.nome == nomePessoa:
                    return button, pessoa
            self.telaPessoas.mostra_mensagem("Pessoa não encontrada. Tente Novamente!")
        return button, None

    def listarPessoas(self):
        self.telaPessoas.listarPessoas(self.pessoas)

    def detalharPessoa(self):
        button, pessoa = self.buscarPessoa()
        if pessoa is None:
            return
        info = {
            'nome': pessoa.nome,
            'sexo': pessoa.sexo,
            'nacionalidade': pessoa.nacionalidade,
            'nascimento': pessoa.nascimento
        }
        self.telaPessoas.detalharPessoa(info)

    def alterarPessoa(self):
        button, pessoaParaAlterar = self.buscarPessoa()
        if pessoaParaAlterar is None or button in (None, 'Cancelar'):
            return None

        setters = {
            1: pessoaParaAlterar.nomeAlterar,
            2: pessoaParaAlterar.sexoAlterar,
            3: pessoaParaAlterar.nacionalidadeAlterar,
            4: pessoaParaAlterar.nascimentoAlterar
        }
        atributos = {
            1: "Nome",
            2: "Sexo",
            3: "Nacionalidade",
            4: "Data de Nascimento"
        }
        button, codigoAtr = self.telaPessoas.mostraAtributos(atributos)
        if button in (None, 'Cancelar'):
            return None

        for i in codigoAtr.keys():
            if codigoAtr[i]:
                codigoAtr = int(i)
                break

        if codigoAtr in {1, 3}:
            button, novoValor = self.telaPessoas.getString(f"Novo(a) {atributos[codigoAtr]}")
            if button in (None, 'Cancelar'):
                return None
            valor = novoValor['key']
        elif codigoAtr == 2:
            button, novoValor1 = self.telaPessoas.getSexo(f'Novo(a) {atributos[codigoAtr]}')
            if button in (None, 'Cancelar'):
                return None
            valor = 'Masculino' if novoValor1['M'] else 'F'
        elif codigoAtr == 4:
            button, novoValor = self.telaPessoas.getDate(f"Novo(a) {atributos[codigoAtr]}")
            if button in (None, 'Cancelar'):
                return None
            partes = novoValor['key'].split('/')
            valor = date(int(partes[2]), int(partes[1]), int(partes[0]))

        funcao = setters[codigoAtr]
        funcao(valor)
        salvar(self.__pessoas, 'pessoas.pkl')
        self.telaPessoas.mostra_mensagem(f"\n✅ Atributo '{atributos[codigoAtr]}' alterado para '{valor}' com sucesso!")
