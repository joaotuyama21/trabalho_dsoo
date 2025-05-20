from datetime import date
from Limite.Tela import Tela

class TelaMembroAcademia(Tela):
    def __init__(self, controladorMembrosAcademia):
        self.__controladorMembrosAcademia = controladorMembrosAcademia

    @property
    def controladorMembrosAcademia(self):
        return self.__controladorMembrosAcademia

    def exibirMenuMembros(self):
        print("\n--- Membros da Academia ---")
        print("1. Incluir Membro")
        print("2. Remover Membro")
        print("3. Alterar Membro")
        print("0. Sair")
        return int(input("Escolha: ").strip())
    
    def incluirMembroInfo(self):
        print("\n--- Cadastro de Membro ---")
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
    
    #def delMembroInfo(self):

    def buscarMembroAcademiaInfo(self):
        while True:
            try:
                id = int(input("Id do membro: ").strip())
                return id
            except ValueError as e:
                print(f"Erro: {e}. Tente novamente.")

    def alterarAtributoMembroAcademia(self, atributos):
        print("--- Atributos ---")
        print("0. Sair")
        for i in range(1, len(atributos)+1):
            print(f"{i}. {atributos[i-1]}")
        return int(input("Selcione o atributo: "))