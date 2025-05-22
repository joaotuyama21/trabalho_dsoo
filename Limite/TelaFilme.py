from Limite.Tela import Tela

class TelaFilme(Tela):
    def  __init__(self, controladorFilme):
        self.__controladorFilme = controladorFilme
    
    def exibirMenu(self):
        print("\n--- Filmes ---")
        print("1. Incluir Filme")
        print("2. Remover Filme")
        print("3. Listar Filmes")
        print("4. Detalhar Filme")
        print("0. Sair")
        return int(input("Escolha: ").strip())
    
    def addFilmeInfo(self):
        print("--- Cadastrar Filme ---")
        titulo = input("Titulo: ")
        ano = self.getInt("Ano: ")
        sinopse = input("Sinopse: ")
        genero = input("Genero: ")
        return {"titulo": titulo, "ano": ano, "sinopse": sinopse, "genero": genero}
