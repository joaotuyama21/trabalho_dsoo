from datetime import date
from sistema_oscar import SistemaOscar
from entidades import *

class Interface:
    def __init__(self, sistema: SistemaOscar):
        self.sistema = sistema

    def exibir_menu_principal(self):
        while True:
            print("\n--- Sistema de Votação do Oscar ---")
            print("1. Registrar Voto")
            print("2. Relatório de Vencedores")
            print("3. Nova Indicação")
            print("4. Cadastrar Membro")
            print("5. Remover Membro")
            print("6. Listar Membros")
            print("0. Sair")

            opcao = input("Escolha: ").strip()

            match opcao:
                case "1": self.registrar_voto()
                case "2": self.gerar_relatorio()
                case "3": self.menu_indicacoes()
                case "4": self.cadastrar_membro()
                case "5": self.remover_membro()
                case "6": self.listar_membros()
                case "0": break
                case _: print("Opção inválida!")

    def menu_indicacoes(self):
        print("\n--- Tipos de Indicação ---")
        print("1. Filme")
        print("2. Ator")
        print("3. Diretor")
        escolha = input("Escolha o tipo: ").strip()

        match escolha:
            case "1": self.indicar_filme()
            case "2": self.indicar_ator()
            case "3": self.indicar_diretor()
            case _: print("Opção inválida!")

    def indicar_filme(self):
        print("\n--- Indicação de Filme ---")
        titulo = input("Título do Filme: ").strip()
        ano = int(input("Ano de Lançamento: "))
        diretor = input("Diretor: ").strip()

        if not any(d.nome == diretor for d in self.sistema.diretores):
            nacionalidade = input(f"Nacionalidade de {diretor}: ").strip()
            self.sistema.diretores.append(Diretor(diretor, nacionalidade, titulo))

        novo_filme = Filme(titulo, diretor, ano, ["Melhor Filme"])
        self.sistema.filmes.append(novo_filme)

        categoria = next(c for c in self.sistema.categorias if c.nome == "Melhor Filme")
        self.sistema.indicacoes.append(Indicacao(categoria, ano, novo_filme))
        print(f"\n✅ Filme '{titulo}' indicado com sucesso!")

    def indicar_ator(self):
        print("\n--- Indicação de Ator ---")
        nome = input("Nome do Ator: ").strip()
        filme = input("Filme: ").strip()
        nacionalidade = input("Nacionalidade: ").strip()

        if not self.sistema.buscar_filme_por_titulo(filme):
            print("\n⚠️ Filme não cadastrado. O ator será indicado mesmo assim.")
            ano = int(input("Ano do Filme para a indicação: "))
        else:
            ano = self.sistema.buscar_filme_por_titulo(filme).ano

        self.sistema.atores.append(Ator(nome, nacionalidade, filme))
        categoria = next(c for c in self.sistema.categorias if c.nome == "Melhor Ator")
        self.sistema.indicacoes.append(Indicacao(categoria, ano, Ator(nome, nacionalidade, filme)))
        print(f"\n✅ Ator '{nome}' indicado com sucesso!")

    def indicar_diretor(self):
        print("\n--- Indicação de Diretor ---")
        nome = input("Nome do Diretor: ").strip()
        filme = input("Filme: ").strip()
        nacionalidade = input("Nacionalidade: ").strip()

        if not self.sistema.buscar_filme_por_titulo(filme):
            print("\n⚠️ Filme não cadastrado. O diretor será indicado mesmo assim.")
            ano = int(input("Ano do Filme para a indicação: "))
        else:
            ano = self.sistema.buscar_filme_por_titulo(filme).ano

        self.sistema.diretores.append(Diretor(nome, nacionalidade, filme))
        categoria = next(c for c in self.sistema.categorias if c.nome == "Melhor Direção")
        self.sistema.indicacoes.append(Indicacao(categoria, ano, Diretor(nome, nacionalidade, filme)))
        print(f"\n✅ Diretor '{nome}' indicado com sucesso!")

    def cadastrar_membro(self):
        print("\n--- Cadastro de Membro ---")
        nome = input("Nome Completo: ").strip()

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

        novo_membro = MembroAcademia(nome, nascimento, nacionalidade)
        self.sistema.membros.append(novo_membro)
        print(f"\n✅ Membro '{nome}' cadastrado com ID {novo_membro.id}!")

    def remover_membro(self):
        print("\n--- Remover Membro ---")
        if not self.sistema.membros:
            print("Nenhum membro cadastrado.")
            return

        self.listar_membros()
        try:
            id_remover = int(input("Digite o ID do membro a ser removido: "))
        except ValueError:
            print("ID inválido.")
            return

        for i, membro in enumerate(self.sistema.membros):
            if membro.id == id_remover:
                nome = membro.nome
                del self.sistema.membros[i]
                print(f"\n✅ Membro '{nome}' removido com sucesso!")
                return
        print("\n❌ Membro não encontrado.")

    def listar_membros(self):
        print("\n--- Membros Cadastrados ---")
        if not self.sistema.membros:
            print("Nenhum membro cadastrado.")
            return

        for membro in self.sistema.membros:
            nascimento_formatado = membro.nascimento.strftime("%d/%m/%Y")
            print(f"ID: {membro.id} | Nome: {membro.nome} | Nascimento: {nascimento_formatado} | Nacionalidade: {membro.nacionalidade}")

    def registrar_voto(self):
        print("\n--- Registrar Voto ---")
        if not self.sistema.membros:
            print("Nenhum membro cadastrado.")
            return

        try:
            id_membro = int(input("ID do Membro: "))
        except ValueError:
            print("ID inválido.")
            return

        membro = self.sistema.buscar_membro_por_id(id_membro)
        if not membro:
            print("Membro não encontrado!")
            return

        print("\nCategorias Disponíveis:")
        for i, cat in enumerate(self.sistema.categorias, 1):
            print(f"{i}. {cat.nome}")

        try:
            escolha = int(input("Escolha a categoria: ")) - 1
            categoria = self.sistema.categorias[escolha]
        except (ValueError, IndexError):
            print("Categoria inválida.")
            return

        indicacoes = self.sistema.buscar_indicacoes_por_categoria(categoria)
        if not indicacoes:
            print("Nenhum indicado nesta categoria.")
            return

        print("\nIndicados:")
        for i, ind in enumerate(indicacoes, 1):
            if isinstance(ind.indicado, Filme):
                nome = ind.indicado.titulo
            elif isinstance(ind.indicado, Ator) or isinstance(ind.indicado, Diretor):
                nome = ind.indicado.nome
            else:
                nome = str(ind.indicado)
            print(f"{i}. {nome}")

        try:
            escolha_ind = int(input("Escolha o indicado: ")) - 1
            indicado = indicacoes[escolha_ind].indicado
        except (ValueError, IndexError):
            print("Indicado inválido.")
            return

        try:
            self.sistema.registrar_voto(categoria, membro, indicado)
            print("\n✅ Voto registrado com sucesso!")
        except ValueError as e:
            print(f"\n❌ Erro: {e}")

    def gerar_relatorio(self):
        print("\n--- Relatório de Vencedores ---")
        vencedores = self.sistema.determinar_vencedores()
        if not vencedores:
            print("Nenhum voto registrado ainda.")
        else:
            for categoria, vencedor in vencedores.items():
                print(f"{categoria}: {vencedor}")
