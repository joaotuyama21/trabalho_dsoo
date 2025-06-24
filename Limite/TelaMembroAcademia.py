from datetime import date
from Limite.Tela import Tela
import PySimpleGUI as sg


class TelaMembroAcademia(Tela):
    def __init__(self, controladorMembrosAcademia):
        self.__controladorMembrosAcademia = controladorMembrosAcademia
        self.__window = None
        self.init_opcoes()

    @property
    def window(self):
        return self.__window
    
    @window.setter
    def window(self, janela):
        if isinstance(janela, sg.Window):
            self.__window = janela

    @property
    def controladorMembrosAcademia(self):
        return self.__controladorMembrosAcademia

    def init_opcoes(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('Menu de Membros', font=("Helvica", 20))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Adicionar Membro', "RD1", key='1')],
        [sg.Radio('Deletar Membro', "RD1", key='2')],
        [sg.Radio('Listar Membro', "RD1", key='3')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Menu de Membros').Layout(layout)

    def exibirMenuMembros(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        # Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def initOpcoesIncluirMembro(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Incluir Membro', font=("Helvica", 20))],
            [sg.Text('Preencha as informações', font=("Helvica", 15))],
            [sg.Input('Nome', key='nome')],
            [sg.Input('Nacionalidade', key='nacionalidade')],
            [sg.Radio('Masculino', 'SEXO', key='M'),
                sg.Radio('Feminino', 'SEXO', key='F')],
            [sg.Input(key='nascimento', size=(20,1)), 
                sg.CalendarButton('Data de Nascimento', target='nascimento', format='%d/%m/%Y')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Incluir Membro').Layout(layout)

    def incluirMembroInfo(self):
        self.initOpcoesIncluirMembro()
        button, values = self.open()
        self.close()
        return button, values
    
    #def delMembroInfo(self):

    def initOpcoesBuscarMembro(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Buscar Membro', font=("Helvica", 20))],
            [sg.Text('Preencha os dados abaixo: ', font=("Helvica", 15))],
            [sg.Input('Nome: ', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Buscar Membro').Layout(layout)

    def buscarMembroAcademiaInfo(self):
        self.initOpcoesBuscarMembro()
        button, value = self.open()
        self.close()
        return button, value

    def alterarAtributoMembroAcademia(self, atributos):
        print("\n --- Atributos ---")
        for i in atributos.keys():
            print(f"{i}. {atributos[i]}")
        return int(input("Selcione o atributo: "))
    
    def initOpcoesListarMembros(self, membros):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [ [sg.Text('Lista de Membros', font=("Helvica", 20))] ]
        for membro in membros:
            layout.append([sg.Text(f'{membro.id} - {membro.nome}', font=("Helvica", 12))])
        layout.append([sg.Button('Confirmar'), sg.Cancel('Cancelar')])
        self.window = sg.Window('Lista de Membros').Layout(layout)

    def listarMembros(self, membros):
        self.initOpcoesListarMembros(membros)
        self.open()
        self.close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()