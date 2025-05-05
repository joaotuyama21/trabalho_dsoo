from Controle.ControladorMembroAcademia import ControladorMembroAcademia
from datetime import date

class TelaMembrosAcademia():
    def __init__(self, controladorMembrosAcademia: ControladorMembroAcademia):
        self.__controladorMembrosAcademia = controladorMembrosAcademia

    @property
    def controladorMembrosAcademia(self):
        return self.__controladorMembrosAcademia

    def exibir_menu_membros(self):
        print("\n--- Membros da Academia ---")
        print("1. Incluir Membro")
        print("2. Remover Membro")
        print("3. Listar Membros")
        print("0. Sair")
        return input("Escolha: ").strip()
    
    def incluir_membro_info(self):
        print("\n--- Cadastro de Membro ---")
        nome = input("Nome Completo: ").strip()
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
        return [nome, nascimento, nacionalidade]
