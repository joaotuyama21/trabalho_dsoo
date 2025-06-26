import PySimpleGUI as sg
from Limite.Tela import Tela

class TelaVoto(Tela):
    def __init__(self, controladorVoto):
        self.__controladorVoto = controladorVoto
        self.__window = None
        self.init_opcoes()

    @property
    def controladorVoto(self):
        return self.__controladorVoto
    
    @property
    def window(self):
        return self.__window
    
    @window.setter
    def window(self, janela):
        self.__window = janela

    def init_opcoes(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Menu de Votos', font=("Helvica", 20))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Adicionar Voto', "RD1", key='1')],
            [sg.Radio('Remover Voto', "RD1", key='2')],
            [sg.Radio('Listar Votos', "RD1", key='3')],
            #[sg.Radio('Detalhar Voto', "RD1", key='4')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Menu de Votos').Layout(layout)

    def exibirMenu(self):
        self.init_opcoes()
        button, values = self.open()
        opcao = 0
        for i in values.keys():
            if values[i]:
                opcao = int(i)
                break
        self.close()
        return button, opcao

    def selecionar(self, list) -> int:
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Escolha sua Opção', font=("Helvica", 20))]
        ]
        for i in range(len(list)):
            layout.append([sg.Radio(f'{i+1} - {list[i]}', "RD1", key=f'{i+1}')])
        layout.append([sg.Button('Confirmar'), sg.Cancel('Cancelar')])
        self.window = sg.Window('Menu de Votos').Layout(layout)
        button, values = self.open()

        for i in values.keys():
            if values[i]:
                values = int(i) - 1
                break
        self.close()
        return button, values

    def listarVotos(self, detalhes):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Lista de Votos', font=("Helvica", 20))]
        ]
        for i in range(len(detalhes)):
            layout.append([sg.Text(f"{i+1} - Indicado: {detalhes[i]['Nome']} - {detalhes[i]['Categoria']} - Membro: {detalhes[i]['Membro']}",font=("Helvica", 10))])

        layout.append([sg.Button('Confirmar'), sg.Cancel('Cancelar')])
        self.window = sg.Window('Menu de Votos').Layout(layout)
        self.open()
        self.close()

    def open(self):
        button, values = self.window.Read()
        return button, values
    
    def close(self):
        self.window.close()