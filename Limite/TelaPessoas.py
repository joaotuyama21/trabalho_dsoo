from Limite.Tela import Tela
from datetime import date

class TelaPessoas(Tela):
    def __init__(self, controladorPessoas):
        self.__controladorPessoas = controladorPessoas

    def exibirMenu(self):
        print("\n--- Pessoas ---")
        print("1. Incluir Pessoa")
        print("2. Remover Pessoa")
        print("3. Listar Pessoas")
        print("4. Detalhar Pessoa")
        print("5. Alterar Pessoa")
        print("0. Sair")
        return int(input("Escolha: ").strip())
    
    def addPessoaInfo(self):
        print("\n--- Cadastro de Pessoa ---")
        nome = input("Nome Completo: ").strip()
        sexo = input("Sexo: ").strip()
        while True:
            try:
                dia = int(input("Dia de Nascimento (DD): "))
                mes = int(input("Mês de Nascimento (MM): "))
                ano = int(input("Ano de Nascimento (AAAA): "))
                nascimento = date(ano, mes, dia)
                break
            except ValueError as e:
                print(f"Erro: {e}. Tente novamente.")
        nacionalidade = input("Nacionalidade: ").strip()
        return {"nome": nome, "sexo": sexo, "nascimento": nascimento, "nacionalidade": nacionalidade}
    
    def mostraAtributos(self, atributos: dict):
        print("--- Atributos ---")
        for i in atributos.keys():
            print(f"{i}. {atributos[i]}")
        return self.getInt("Escolha o Atributo: ")