class TelaVoto:
    def __init__(self, controladorVoto):
        self.__controladorVoto = controladorVoto

    def exibirMenu(self):
        print("\n--- Menu Votos ---")
        print("1 - Adicionar Voto")
        print("2 - Remover Voto")
        print("3 - Listar Votos")
        print("4 - Detalhar Voto")
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
