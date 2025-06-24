from abc import ABC, abstractmethod
from datetime import date
import PySimpleGUI as sg

class Tela(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def getString(self, mensagem: str):
        while True:
            output = input(mensagem)
            if isinstance(output, str):
                return output
            print("Valor inválido. Tente Novamente!")
    
    def getDate(self, mensagem):
        while True:
            print(mensagem)
            dia = input("Dia (DD): ")
            mes = input("Mês (MM): ")
            ano = input("Ano (AAAA): ")
            if isinstance(dia, int) and isinstance(mes, int) and isinstance(ano, int):
                return date(ano, mes, dia)
            else:
                print("Data inválida. Tente Novamente!")

    def getInt(self, mensagem):
        while True:
            output = int(input(mensagem))
            if isinstance(output, int):
                return output
            print("Valor invalido! Tente Novamente.")