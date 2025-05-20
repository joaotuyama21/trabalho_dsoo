from Limite.Tela import Tela

class TelaSistema(Tela):
    def __init__(self, controladorSistema):
        self.__controladorSistema = controladorSistema
        
    def exibirMenuPrincipal(self):
        print("\n--- Sistema de Votação do Oscar ---")
        print("1. Membros")
        print("2. ----")
        print("3. ----")
        return int(input("Escolha: ").strip())
        