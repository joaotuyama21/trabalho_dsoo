from Limite.TelaPessoas import TelaPessoas
from Entidades.Pessoa import Pessoa
from datetime import date

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
                funcao()
            else:
                self.telaPessoas.mostra_mensagem("Opção inválida!")

    def addPessoa(self):
        info = self.telaPessoas.addPessoaInfo()
        novaPessoa = Pessoa(info["nome"], info["sexo"], info["nacionalidade"], info["nascimento"])
        if not self.verificarSeHaPessoaDuplicado(novaPessoa):
            self.pessoas.append(novaPessoa)
            self.telaPessoas.mostraMensagem(f"\n✅ Pessoa '{novaPessoa.nome}' cadastrado com ID {novaPessoa.id}!")
        else:
            self.telaPessoas.mostraMensagem(f"\n Pessoa '{novaPessoa.nome}' já cadastrado!")

    def verificarSeHaPessoaDuplicado(self, copia: Pessoa) -> bool:
        for pessoa in self.pessoas:
            if pessoa.nome == copia.nome:
                return True
        return False

    def delPessoa(self):
        self.telaPessoas.mostraMensagem("\n--- Remover Pessoa ---")
        pessoaRemovida = self.buscarPessoa()
        self.pessoas.remove(pessoaRemovida)
        self.telaPessoas.mostraMensagem(f"\n✅ Pessoa '{pessoaRemovida.nome}' foi removdo com sucesso!")

    def buscarPessoa(self) -> Pessoa:
        while True:
            id = self.telaPessoas.getInt("ID da Pessoa: ")
            for pessoa in self.pessoas:
                if pessoa.id == id:
                    return pessoa
            print("Pessoa não encontrada! Tente novamente.")

    def listarPessoas(self):
        self.telaPessoas.mostraMensagem("\n--- Lista de Pessoas ---")
        for pessoa in self.pessoas:
            self.telaPessoas.mostraMensagem(f"{pessoa.id}. {pessoa.nome}")
        input()

    def detalharPessoa(self):
        self.telaPessoas.mostraMensagem("\n--- Detalhar Pessoa --- ")
        pessoa = self.buscarPessoa()
        self.telaPessoas.mostraMensagem(f"Nome: {pessoa.nome}")
        self.telaPessoas.mostraMensagem(f"Sexo: {pessoa.sexo}")
        self.telaPessoas.mostraMensagem(f"Nacionalidade: {pessoa.nacionalidade}")
        self.telaPessoas.mostraMensagem(f"Data de Nascimento: {pessoa.nascimento}")
        input()

    def alterarPessoa(self):
        self.telaPessoas.mostraMensagem("\n--- Alterar Pessoa ---")
        pessoaParaAlterar = self.buscarPessoa()
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
        codigoAtr = self.telaPessoas.mostraAtributos(atributos)

        if codigoAtr in {1,2,3}:
            novoValor = self.telaPessoas.getString(f"Novo(a) {atributos[codigoAtr]}: ")
        elif codigoAtr == 4:
            novoValor = self.telaPessoas.getDate(f"Novo(a) {atributos[codigoAtr]}: ")

        funcao = setters[codigoAtr]
        funcao(novoValor)
        self.telaPessoas.mostraMensagem(f"\n✅ Atributo '{atributos[codigoAtr]}' alterado para '{novoValor}' com sucesso!")
