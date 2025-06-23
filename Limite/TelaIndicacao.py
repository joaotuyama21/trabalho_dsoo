class TelaIndicacao:
    def __init__(self, controladorIndicacao):
        self.__controladorIndicacao = controladorIndicacao

    def exibirMenu(self):
        print("\n--- Menu Indicações ---")
        print("1 - Adicionar Indicação")
        print("2 - Remover Indicação")
        print("3 - Listar Indicações")
        print("4 - Detalhar Indicação")
        print("0 - Voltar")
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            opcao = -1
        return opcao

    def mostraMensagem(self, msg):
        print(msg)

    def getInt(self, msg):
        while True:
            try:
                return int(input(msg))
            except ValueError:
                print("Digite um número inteiro válido.")

    def getString(self, msg):
        return input(msg)
