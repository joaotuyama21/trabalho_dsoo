from Limite.Tela import Tela
import PySimpleGUI as sg

class TelaSistema(Tela):
    def __init__(self, controladorSistema):
        self.__controladorSistema = controladorSistema

    def exibirMenuPrincipal(self):
        '''
        print("\n--- Sistema de Votação do Oscar ---")
        print("1. Membros")
        print("2. Pessoas")
        print("3. Filmes")
        print("4. Categorias")
        print("5. Participantes")
        print("6. Indicações")
        print("7. Votos")
        print("8. Resultados Finais")
        print("0. Sair")
        '''
        
        # Define o layout da janela
        layout = [[sg.Button('My first Button!'), sg.Button('Disabled Button!', disabled=True)]]


        # Cria a janela
        window = sg.Window("Menu Principal").Layout(layout)

        # Loop de eventos
        while True:
            event, values = window.read()
            
            if event in (sg.WIN_CLOSED, "Sair"):
                break
            else:
                sg.popup(f"Você clicou em: {event}", title="Ação")

        # Fecha a janela
        window.close()

        # return int(input("Escolha: ").strip())

    def mostrar_resultados(self, resultados):
        print("\n=== RESULTADOS OFICIAIS ===")
        for categoria, dados in resultados.items():
            print(f"\n{categoria.upper()}")
            print(f"Vencedor: {dados['vencedor']}")
            print(f"Votos recebidos: {dados['votos']}/{dados['total_votos']}")
            print("="*40)
