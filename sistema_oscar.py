from entidades import *
from typing import List, Dict

class SistemaOscar:
    def __init__(self):
        self.membros: List[MembroAcademia] = []
        self.filmes: List[Filme] = []
        self.atores: List[Ator] = []
        self.diretores: List[Diretor] = []
        self.categorias: List[Categoria] = [
            Categoria("Melhor Filme", "filme"),
            Categoria("Melhor Direção", "diretor"),
            Categoria("Melhor Ator", "ator")
        ]
        self.indicacoes: List[Indicacao] = []
        self.votos: List[Voto] = []

    def buscar_membro_por_id(self, id_membro: int) -> MembroAcademia:
        return next((m for m in self.membros if m.id == id_membro), None)

    def buscar_indicacoes_por_categoria(self, categoria: Categoria) -> List[Indicacao]:
        return [i for i in self.indicacoes if i.categoria.nome == categoria.nome]

    def buscar_filme_por_titulo(self, titulo: str) -> Filme:
        return next((m for m in self.filmes if m.titulo == titulo), None)

    def registrar_voto(self, categoria: Categoria, membro: MembroAcademia, indicado):
        if categoria.nome in membro.votos_realizados:
            raise ValueError("Membro já votou nesta categoria")
        self.votos.append(Voto(categoria, membro, indicado))
        membro.votos_realizados.add(categoria.nome)

    def gerar_relatorio_indicacoes(self, ano: int = None, categoria: str = None) -> List[Indicacao]:
        resultado = self.indicacoes
        if ano:
            resultado = [i for i in resultado if i.ano == ano]
        if categoria:
            resultado = [i for i in resultado if i.categoria.nome == categoria]
        return resultado

    def gerar_relatorio_votos(self, categoria: str = None, ano: int = None) -> Dict[str, int]:
        votos_por_indicado = {}
        for voto in self.votos:
            if categoria and voto.categoria.nome != categoria:
                continue
            if ano and hasattr(voto.indicado, 'ano') and voto.indicado.ano != ano:
                continue
            if isinstance(voto.indicado, Diretor) or isinstance(voto.indicado, Ator):
                chave = f"{voto.indicado.nome}"
            else:
                chave = f"{voto.indicado.titulo}"
            votos_por_indicado[chave] = votos_por_indicado.get(chave, 0) + 1
        return votos_por_indicado

    def determinar_vencedores(self) -> Dict[str, str]:
        vencedores = {}
        for categoria in self.categorias:
            votos = self.gerar_relatorio_votos(categoria=categoria.nome)
            if votos:
                vencedor = max(votos, key=votos.get)
                vencedores[categoria.nome] = vencedor
        return vencedores
