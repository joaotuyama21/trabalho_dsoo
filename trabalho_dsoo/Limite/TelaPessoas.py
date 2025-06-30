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
            [sg.Radio('Listar Pessoas', "RD1", key='3')],
            [sg.Radio('Detalhar Pessoa', "RD1", key='4')],
            [sg.Radio('Alterar Pessoas', "RD1", key='5')],
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
    
    def initOpcoesBuscarPessoa(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Buscar Pessoa', font=("Helvica", 20))],
            [sg.Text('Preencha os dados abaixo: ', font=("Helvica", 15))],
            [sg.Input('Nome: ', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Pessoa Membro').Layout(layout)

    def buscarPessoaInfo(self):
        self.initOpcoesBuscarPessoa()
        button, value = self.open()
        self.close()
        return button, value

    def initOpcoesListarPessoas(self, pessoas):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [ [sg.Text('Lista de Pessoas', font=("Helvica", 20))] ]
        for pessoas in pessoas:
            layout.append([sg.Text(f'{pessoas.id} - {pessoas.nome}', font=("Helvica", 12))])
        layout.append([sg.Button('Confirmar'), sg.Cancel('Cancelar')])
        self.window = sg.Window('Lista de Pessoas').Layout(layout)

    def listarPessoas(self, membros):
        self.initOpcoesListarPessoas(membros)
        self.open()
        self.close()

    def initOpcoesDetalharPessoa(self, info):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Detalhar Pessoa', font=("Helvica", 20))],
            [sg.Text(f"Nome: {info['nome']}", font=("Helvica", 15))],
            [sg.Text(f"Sexo: {info['sexo']}", font=("Helvica", 15))],
            [sg.Text(f"Nacionalidade: {info['nacionalidade']}", font=("Helvica", 15))],
            [sg.Text(f"Nascimento: {info['nascimento']}", font=("Helvica", 15))],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Pessoa Membro').Layout(layout)
    
    def detalharPessoa(self, info):
        self.initOpcoesDetalharPessoa(info)
        self.open()
        self.close()

    def initOpcoesMostraAtributos(self, atributos):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [ [sg.Text('Lista de Atributos', font=("Helvica", 20))] ]
        for i in atributos.keys():
            layout.append([sg.Radio(f'{atributos[i]}', 'atr', key = f'{i}')])
        layout.append([sg.Button('Confirmar'), sg.Cancel('Cancelar')])
        self.window = sg.Window('Atributos de Pessoas').Layout(layout)

    def mostraAtributos(self, atributos):
        self.initOpcoesMostraAtributos(atributos)
        button, values = self.open()
        self.close()
        return button, values

    def getString(self, msg):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Novo Valor', font=("Helvica", 20))],
            [sg.Text('Preencha os dados abaixo: ', font=("Helvica", 15))],
            [sg.Input(f'{msg}', key='key')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Pessoa Alterar').Layout(layout)
        button, values = self.open()
        self.close()
        return button, values
    
    def getDate(self, msg):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Novo Valor', font=("Helvica", 20))],
            [sg.Text('Preencha os dados abaixo: ', font=("Helvica", 15))],
             [sg.Input(key='key', size=(20,1)), 
                sg.CalendarButton('Data de Nascimento', target='key', format='%d/%m/%Y')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Pessoa Alterar').Layout(layout)
        button, values = self.open()
        self.close()
        return button, values
    
    def getSexo(self, msg):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Novo Valor', font=("Helvica", 20))],
            [sg.Text('Preencha os dados abaixo: ', font=("Helvica", 15))],
            [sg.Radio('Masculino', 'key', key='M'),
                sg.Radio('Feminino', 'key', key='F')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Pessoa Alterar').Layout(layout)
        button, values = self.open()
        self.close()
        return button, values

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()