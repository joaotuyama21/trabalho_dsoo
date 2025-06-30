from Limite.Tela import Tela
import PySimpleGUI as sg

class TelaCategoria(Tela):
    def __init__(self, controladorCategoria):
        self.__controladorCategoria = controladorCategoria
        self.__window = None
        self.init_opcoes()

    @property
    def controladorCategoria(self):
        return self.__controladorCategoria
    
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
            [sg.Text('Menu de Categoria', font=("Helvica", 20))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Listar Categorias', "RD1", key='3')],
            [sg.Radio('Detalhar Categoria', "RD1", key='4')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Menu de Categoria').Layout(layout)

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

    def addCategoriaInfo(self) -> dict:
        print("\n--- Cadastrar Categoria ---")
        nome = self.getString("Nome da Categoria: ")
        funcao_nome = self.getString("Nome da Função: ")
        funcao_descricao = self.getString("Descrição da Função: ")
        tipo = self.getInt("Digite 1 para categoria de Filme ou 2 para Participante: ")
        e_filme = tipo == 1
        return {
            "nome": nome,
            "funcao_nome": funcao_nome,
            "funcao_descricao": funcao_descricao,
            "e_filme": e_filme
        }

    def listarCategorias(self, categorias):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [[sg.Text('Lista de Categorias', font=("Helvica", 20))]]
        for nome in categorias:
            layout.append([sg.Text(f'{nome}', font=("Helvica", 12))])
        layout.append([sg.Button('Confirmar'), sg.Cancel('Cancelar')])
        self.window = sg.Window('Lista de Categorias').Layout(layout)
        self.open()
        self.close()

    def getString(self, msg):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Novo Valor', font=("Helvica", 20))],
            [sg.Text('Preencha os dados abaixo: ', font=("Helvica", 15))],
            [sg.Input(f'{msg}', key='key')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.window = sg.Window('Detalhes da Categoria').Layout(layout)
        button, values = self.open()
        self.close()
        return button, values

    def detalharCategoria(self,info):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [[sg.Text('Detalhes da Categoria', font=("Helvica", 20))]]
        for i in info.keys():
            layout.append([sg.Text(f'{i} - {info[i]}', font=("Helvica", 15))])
        layout.append([sg.Button('Confirmar')])
        self.window = sg.Window('Detalhes da Categoria').Layout(layout)
        self.open()
        self.close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()