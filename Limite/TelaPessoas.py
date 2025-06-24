from Limite.Tela import Tela
from datetime import date
import PySimpleGUI as sg

class TelaPessoas(Tela):
    def __init__(self, controladorPessoas):
        self.__controladorPessoas = controladorPessoas
        self.__window = None
        self.init_opcoes()

    @property
    def controladorPessoas(self):
        return self.__controladorPessoas
    
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
            [sg.Text('Menu de Pessoas', font=("Helvica", 20))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Adicionar Pessoa', "RD1", key='1')],
            [sg.Radio('Deletar Pessoa', "RD1", key='2')],
            [sg.Radio('Listar Membro', "RD1", key='3')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Menu de Membros').Layout(layout)

    def exibirMenu(self):
        self.init_opcoes()
        button, values = self.open()

        for i in values.keys():
            if values[i]:
                opcao = int(i)
                break
        if button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def initOpcoesIncluirPessoas(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Incluir Pessoa', font=("Helvica", 20))],
            [sg.Text('Preencha as informações', font=("Helvica", 15))],
            [sg.Input('Nome', key='nome')],
            [sg.Input('Nacionalidade', key='nacionalidade')],
            [sg.Radio('Masculino', 'SEXO', key='M'),
                sg.Radio('Feminino', 'SEXO', key='F')],
            [sg.Input(key='nascimento', size=(20,1)), 
                sg.CalendarButton('Data de Nascimento', target='nascimento', format='%d/%m/%Y')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Incluir Pessoa').Layout(layout)

    def AddPessoaInfo(self):
        self.initOpcoesIncluirPessoas()
        button, values = self.open()
        self.close()
        return button, values

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()