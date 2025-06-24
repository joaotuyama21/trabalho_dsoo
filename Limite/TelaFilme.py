from Limite.Tela import Tela
import PySimpleGUI as sg

class TelaFilme(Tela):
    def  __init__(self, controladorFilme):
        self.__controladorFilme = controladorFilme
        self.__window = None
        self.init_opcoes()
    
    @property
    def window(self):
        return self.__window
    
    @property
    def controladorFilme(self):
        return self.__controladorFilme
    
    @window.setter
    def window(self, janela):
        self.__window = janela

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Menu de Filme', font=("Helvica", 20))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Adicionar Filme', "RD1", key='1')],
            [sg.Radio('Deletar Filme', "RD1", key='2')],
            [sg.Radio('Listar Filme', "RD1", key='3')],
            [sg.Radio('Detalhar Filme', "RD1", key='4')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Menu de Filmes').Layout(layout)

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
    
    def addFilmeInfo(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Incluir Filme', font=("Helvica", 20))],
            [sg.Text('Preencha as informações', font=("Helvica", 15))],
            [sg.Input('Titulo', key='titulo')],
            [sg.Input('ano', key='ano')],
            [sg.Input('genero' , key='genero', size=(20,1))], 
            [sg.Input('sinopse' , key='sinopse', size=(20,1))], 
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Incluir Filme').Layout(layout)
        button, values = self.open()
        self.close()
        return button, values
    
    def listarFilmes(self, filmes):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [[sg.Text('Lista de Filmes', font=("Helvica", 20))]]
        for nome in filmes:
            layout.append([sg.Text(f'{nome}', font=("Helvica", 12))])
        layout.append([sg.Button('Confirmar'), sg.Cancel('Cancelar')])
        self.window = sg.Window('Listar Filmes').Layout(layout)
        self.open()
        self.close()

    def buscarFilmeInfo(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Buscar Filme', font=("Helvica", 20))],
            [sg.Text('Preencha os dados abaixo: ', font=("Helvica", 15))],
            [sg.Input('Titulo: ', key='titulo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Buscar Filme').Layout(layout)
        button, value = self.open()
        self.close()
        return button, value
    
    def detalharFilme(self, info):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Detalhar Filme', font=("Helvica", 20))],
            [sg.Text(f"Titulo: {info['titulo']}", font=("Helvica", 12))],
            [sg.Text(f"Ano: {info['ano']}", font=("Helvica", 12))],
            [sg.Text(f"Sinopse: {info['sinopse']}", font=("Helvica", 12))],
            [sg.Text(f"Genero: {info['genero']}", font=("Helvica", 12))],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Detalhar Filme').Layout(layout)

        self.open()
        self.close()

    
    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()