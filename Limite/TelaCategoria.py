from Limite.Tela import Tela

class TelaCategoria(Tela):
    def __init__(self, controladorCategoria):
        self.__controladorCategoria = controladorCategoria

    def exibirMenu(self):
        print("\n--- Categorias ---")
        print("1. Incluir Categoria")
        print("2. Remover Categoria")
        print("3. Listar Categorias")
        print("4. Detalhar Categoria")
        print("0. Sair")
        return int(input("Escolha: ").strip())

    def addCategoriaInfo(self) -> list:
        print("\n--- Cadastrar Categoria ---")
        nome = self.getString("Nome: ")
        funcao = self.getString("Função: ")
        return {"nome": nome, "funcao": funcao}

