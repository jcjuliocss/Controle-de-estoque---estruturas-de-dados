"""Docstring da classe produto."""
from HashTable import HashTable


class Produto:
    """Classe produto."""

    def __init__(self, id_produto, nome,
                 preco, qtd_minima, qtd=0):
        """Construtor."""
        self.descricao = HashTable()
        self.descricao.adiciona('id', id_produto)
        self.descricao.adiciona('nome', nome)
        self.descricao.adiciona('preco', preco)
        self.descricao.adiciona('qtd_minima', qtd_minima)
        self.descricao.adiciona('qtd', qtd)
