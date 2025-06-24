from Limite.Tela import Tela
import PySimpleGUI as sg

class TelaSistema(Tela):
    def __init__(self, controladorSistema):
        self.__controladorSistema = controladorSistema
        self.__window = None
        self.init_opcoes()        

    def init_opcoes(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('Menu Principal', font=("Helvica", 20))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Membros', "RD1", key='1')],
        [sg.Radio('Pessoas', "RD1", key='2')],
        [sg.Radio('Filmes', "RD1", key='3')],
        [sg.Radio('Categorias', "RD1", key='4')],
        [sg.Radio('Participantes', "RD1", key='5')],
        [sg.Radio('Indicações', "RD1", key='6')],
        [sg.Radio('Votos', "RD1", key='7')],
        [sg.Radio('Resultados Finais', "RD1", key='8')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)

    def exibirMenuPrincipal(self):        
        self.init_opcoes()
        button, values = self.open()

        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if values['7']:
            opcao = 7
        if values['8']:
            opcao = 8
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        # Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return  opcao
    
    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def mostrar_resultados(self, resultados):
        print("\n=== RESULTADOS OFICIAIS ===")
        for categoria, dados in resultados.items():
            print(f"\n{categoria.upper()}")
            print(f"Vencedor: {dados['vencedor']}")
            print(f"Votos recebidos: {dados['votos']}/{dados['total_votos']}")
            print("="*40)