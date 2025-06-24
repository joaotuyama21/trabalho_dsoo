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
            opcao == 0
        self.close()
        return opcao

    
    def addPessoaInfo(self):
        print("\n--- Cadastro de Pessoa ---")
        nome = input("Nome Completo: ").strip()
        sexo = input("Sexo: ").strip()
        while True:
            try:
                dia = int(input("Dia de Nascimento (DD): "))
                mes = int(input("Mês de Nascimento (MM): "))
                ano = int(input("Ano de Nascimento (AAAA): "))
                nascimento = date(ano, mes, dia)
                break
            except ValueError as e:
                print(f"Erro: {e}. Tente novamente.")
        nacionalidade = input("Nacionalidade: ").strip()
        return {"nome": nome, "sexo": sexo, "nascimento": nascimento, "nacionalidade": nacionalidade}
    
    def mostraAtributos(self, atributos: dict):
        print("--- Atributos ---")
        for i in atributos.keys():
            print(f"{i}. {atributos[i]}")
        return self.getInt("Escolha o Atributo: ")

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()