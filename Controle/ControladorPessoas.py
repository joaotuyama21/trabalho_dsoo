from Limite.TelaPessoas import TelaPessoas
from Entidades.Pessoa import Pessoa
from datetime import date
from Exceptions.Excecoes import *

class ControladorPessoas:
    def __init__(self, controladorSistema):
        self.__pessoas = []
        self.__controladorSistema = controladorSistema
        self.__telaPessoas = TelaPessoas(self)

        self.__pessoas.append(Pessoa("Leonardo DiCaprio", "Masculino", "Americano", date(1974, 11, 11)))
        self.__pessoas.append(Pessoa("Emma Stone", "Feminino", "Americana", date(1988, 11, 6)))
        self.__pessoas.append(Pessoa("Alejandro González Iñárritu", "Masculino", "Mexicano", date(1963, 8, 15)))

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
                except (InstaciaJaCadastradaException) as e:
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
            self.telaPessoas.mostra_mensagem(f"\n✅ Pessoa '{novaPessoa.nome}' cadastrado com ID {novaPessoa.id}!")
        else:
            raise InstaciaJaCadastradaException

    def verificarSeHaPessoaDuplicado(self, copia: Pessoa) -> bool:
        for pessoa in self.pessoas:
            if pessoa.nome == copia.nome:
                return True
        return False

    def delPessoa(self):
        #self.telaPessoas.mostraMensagem("\n--- Remover Pessoa ---")
        button, pessoaRemovida = self.buscarPessoa()
        try:
            self.pessoas.remove(pessoaRemovida)
        except ValueError or AttributeError:
            self.telaPessoas.mostra_mensagem(f"\n Pessoa '{pessoaRemovida.nome}' não foi removida com sucesso")
        else:
            self.telaPessoas.mostra_mensagem(f"\n✅ Pessoa '{pessoaRemovida.nome}' foi removdo com sucesso!")

    def buscarPessoa(self) -> Pessoa:
        button, values = self.telaPessoas.buscarPessoaInfo()
        nomePessoa = values['nome']
        if button == 'Confirmar':
            for pessoa in self.pessoas:
                if pessoa.nome == nomePessoa:
                    return button, pessoa
            self.telaPessoas.mostra_mensagem("Pessoa não encontrada. Tente Novamente!")
        return button, None
        '''
        while True:
            id = self.telaPessoas.getInt("ID da Pessoa: ")
            for pessoa in self.pessoas:
                if pessoa.id == id:
                    return pessoa
            print("Pessoa não encontrada! Tente novamente.")
        '''
            
    def listarPessoas(self):
        self.telaPessoas.mostraMensagem("\n--- Lista de Pessoas ---")
        for pessoa in self.pessoas:
            self.telaPessoas.mostraMensagem(f"{pessoa.id}. {pessoa.nome}")
        input()

    def listarPessoas(self):
        self.telaPessoas.listarPessoas(self.pessoas)

    def detalharPessoa(self):
        button, pessoa = self.buscarPessoa()
        info = {
                'nome': pessoa.nome,
                'sexo': pessoa.sexo,
                'nacionalidade': pessoa.nacionalidade,
                'nascimento': pessoa.nascimento
        }
        self.telaPessoas.detalharPessoa(info)

    def alterarPessoa(self):
        button, pessoaParaAlterar = self.buscarPessoa()
        if button in (None, 'Cancelar'):
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

        if codigoAtr in {1,3}:
            button, novoValor = self.telaPessoas.getString(f"Novo(a) {atributos[codigoAtr]}")
            if button in (None, 'Cancelar'):
                return None
        elif codigoAtr in {2}:
            button, novoValor1 = self.telaPessoas.getSexo(f'Novo(a) {atributos[codigoAtr]}')
            if button in (None, 'Cancelar'):
                return None
            for i in novoValor1.keys():
                if novoValor1[i]:
                    novoValor = {}
                    novoValor['key'] = i
                    break
        elif codigoAtr in {4}:
            button, novoValor = self.telaPessoas.getDate(f"Novo(a) {atributos[codigoAtr]}")
            if button in (None, 'Cancelar'):
                return None
            novoValor['key'] = novoValor['key'].split('/')
            novoValor['key'] = date(int(novoValor['key'][2]), int(novoValor['key'][1]), int(novoValor['key'][0]))

        funcao = setters[codigoAtr]
        funcao(novoValor['key'])
        self.telaPessoas.mostra_mensagem(f"\n✅ Atributo '{atributos[codigoAtr]}' alterado para '{novoValor['key']}' com sucesso!")
