class NenhumMembroCadastradoException(Exception):
    def __init__(self):
        super().__init__("Nenhum membro cadastrado")

class NenhumaCategoriaCadastradaException(Exception):
    def __init__(self):
        super().__init__("Nenhuma Categoria cadastrado")

class NenhumFilmeCadastradoException(Exception):
    def __init__(self):
        super().__init__("Nenhum Filme cadastrado")

class InstaciaJaCadastradaException(Exception):
    def __init__(self):
        super().__init__("Esse elemento já foi cadastrado")

class InformacoesInvalidasException(Exception):
    def __init__(self):
        super().__init__("Informações Inválidas")

class NenhumParticipanteCadastradoException(Exception):
    def __init__(self):
        super().__init__("Nenhum Paricipante cadastrado")