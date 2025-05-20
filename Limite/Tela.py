from abc import ABC, abstractmethod

class Tela(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def mostraMensagem(self, mensagem: str):
        print(mensagem)