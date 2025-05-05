from Controle.ControladorSistema import ControladorSistema

class TelaSistema():
    def __init__(self, controladorSistema: ControladorSistema):
        self.__controladorSistema = controladorSistema
        
    def exibir_menu_principal(self):
        print("\n--- Sistema de Votação do Oscar ---")
        print("1. Membros")
        print("2. ----")
        print("3. ----")
        return input("Escolha: ").strip()
        