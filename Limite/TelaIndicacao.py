from Limite.Tela import Tela
import PySimpleGUI as sg

class TelaIndicacao(Tela):
    def __init__(self, controladorIndicacao):
        self.__controladorIndicacao = controladorIndicacao
        self.__window = None
        self.init_opcoes()

    @property
    def controladorIndicacao(self):
        return self.__controladorIndicacao
    
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
            [sg.Text('Menu de Indicação', font=("Helvica", 20))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Adicionar Indicação', "RD1", key='1')],
            [sg.Radio('Remover Indicação', "RD1", key='2')],
            [sg.Radio('Listar Indicações', "RD1", key='3')],
            #[sg.Radio('Detalhar Indicação', "RD1", key='4')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Menu de Indicações').Layout(layout)

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
        self.window = sg.Window('Menu de Indicações').Layout(layout)
        button, values = self.open()

        for i in values.keys():
            if values[i]:
                values = int(i) - 1
                break
        self.close()
        return button, values

    def listarIndicacoes(self, detalhes):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Lista de Indicações', font=("Helvica", 20))]
        ]
        for i in range(len(detalhes)):
            if detalhes[i]['eh_filme']:
                layout.append([sg.Text(f"{i+1} - Filme: {detalhes[i]['Filme']} - {detalhes[i]['Categoria']} - {detalhes[i]['Membro']}",font=("Helvica", 10))])
            else:
                layout.append([sg.Text(f"{i+1} - Participante: {detalhes[i]['Participante']} - {detalhes[i]['Categoria']} - {detalhes[i]['Membro']}", font=("Helvica", 10))])

        layout.append([sg.Button('Confirmar'), sg.Cancel('Cancelar')])
        self.window = sg.Window('Menu de Indicações').Layout(layout)
        self.open()
        self.close()

    def getInt(self, msg):
        while True:
            try:
                return int(input(msg))
            except ValueError:
                print("Digite um número inteiro válido.")

    def getString(self, msg):
        return input(msg)

    def open(self):
        button, values = self.window.Read()
        return button, values
    
    def close(self):
        self.window.close()