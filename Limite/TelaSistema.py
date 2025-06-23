from Limite.Tela import Tela

class TelaSistema(Tela):
    def __init__(self, controladorSistema):
        self.__controladorSistema = controladorSistema

    def exibirMenuPrincipal(self):
        print("\n--- Sistema de Votação do Oscar ---")
        print("1. Membros")
        print("2. Pessoas")
        print("3. Filmes")
        print("4. Categorias")
        print("5. Participantes")
        print("6. Indicações")
        print("7. Votos")
        print("8. Resultados Finais")
        print("0. Sair")
        return int(input("Escolha: ").strip())

    def mostrar_resultados(self, resultados):
        print("\n=== RESULTADOS OFICIAIS ===")
        for categoria, dados in resultados.items():
            print(f"\n{categoria.upper()}")
            print(f"Vencedor: {dados['vencedor']}")
            print(f"Votos recebidos: {dados['votos']}/{dados['total_votos']}")
            print("="*40)
