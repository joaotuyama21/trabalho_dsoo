from Limite.Tela import Tela

class TelaSistema(Tela):
    def __init__(self, controladorSistema):
        self.__controladorSistema = controladorSistema
        
    def exibirMenuPrincipal(self):
        print("\n--- Sistema de Votação do Oscar ---")
        print("1. Membros")
        print("2. Pessoas")
        print("3. Filmes")
        print("4. Categorias")
        return int(input("Escolha: ").strip())
        