from Limite.Tela import Tela
from datetime import date
import PySimpleGUI as sg

class TelaParticipante(Tela):
    def __init__(self, controladorParticipante):
        self.__controladorParticipante = controladorParticipante
        self.__window = None
        self.init_opcoes()

    @property
    def controladorParticipante(self):
        return self.__controladorParticipante
    
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
            [sg.Text('Menu de Participante', font=("Helvica", 20))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Adicionar Participante', "RD1", key='1')],
            [sg.Radio('Deletar Participante', "RD1", key='2')],
            [sg.Radio('Listar Participante', "RD1", key='3')],
            #[sg.Radio('Detalhar Participante', "RD1", key='4')],
            [sg.Radio('Alterar Participante', "RD1", key='5')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Menu de Participante').Layout(layout)

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

    def initOpcoesIncluirFuncao(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Incluir Função', font=("Helvica", 20))],
            [sg.Text('Preencha as informações', font=("Helvica", 15))],
            [sg.Input('Função (ex: Ator, Diretor):', key='nome')],
            [sg.Input('Descrição da Função:', key='descricao')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Incluir Funcao').Layout(layout)

    def selecionar(self, list) -> int:
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Escolha sua Opção', font=("Helvica", 20))]
        ]
        for i in range(len(list)):
            layout.append([sg.Radio(f'{i+1} - {list[i]}', "RD1", key=f'{i+1}')])
        layout.append([sg.Button('Confirmar'), sg.Cancel('Cancelar')])
        self.window = sg.Window('Menu de Participantes').Layout(layout)
        button, values = self.open()

        for i in values.keys():
            if values[i]:
                values = int(i) - 1
                break
        self.close()
        return button, values

    def addFuncaoInfo(self):
        self.initOpcoesIncluirFuncao()
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

    def initOpcoesListarParticipante(self, part):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [ [sg.Text('Lista de Participações', font=("Helvica", 20))] ]
        for p, i in enumerate(part, 1):
            layout.append([sg.Text(f'{p} - {i}', font=("Helvica", 10))])
        layout.append([sg.Button('Confirmar'), sg.Cancel('Cancelar')])
        self.window = sg.Window('Lista de Paticipações').Layout(layout)

    def listarParticipantes(self, participante):
        self.initOpcoesListarParticipante(participante)
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
        self.window = sg.Window('Atributos de Participante').Layout(layout)

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