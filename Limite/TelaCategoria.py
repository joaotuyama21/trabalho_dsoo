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

def addCategoriaInfo(self) -> dict:
    print("\n--- Cadastrar Categoria ---")
    nome = self.getString("Nome da Categoria: ")
    funcao_nome = self.getString("Nome da Função: ")
    funcao_descricao = self.getString("Descrição da Função: ")
    tipo = self.getInt("Digite 1 para categoria de Filme ou 2 para Participante: ")
    e_filme = tipo == 1
    return {
        "nome": nome,
        "funcao_nome": funcao_nome,
        "funcao_descricao": funcao_descricao,
        "e_filme": e_filme
    }
