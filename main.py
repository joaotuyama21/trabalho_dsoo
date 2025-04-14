from sistema_oscar import SistemaOscar
from interface import Interface

def main():
    sistema = SistemaOscar()
    interface = Interface(sistema)
    interface.exibir_menu_principal()

if __name__ == "__main__":
    main()
