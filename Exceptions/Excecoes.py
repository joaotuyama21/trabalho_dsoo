class IndiceInvalidoException(Exception):
    def __init__(self):
        super().__init__('Indice Inválido')

class InstaciaJaCadastradaException(Exception):
    def __init__(self):
        super().__init__("Esse elemento já foi cadastrado")

class InformacoesInvalidasException(Exception):
    def __init__(self):
        super().__init__("Informações Inválidas")

class MembroJaVotouNessaCategoriaException(Exception):
    def __init__(self):
        super().__init__('Esse membro já votou nessa categoria')

class SemCadastrosException(Exception):
    def __init__(self):
        super().__init__('Sem cadastros necessários para realizar a ação')