"""."""
from LDDE import LDDE
from LES import LES
from Produto import Produto


class Estoque:
    """Classe estoque."""

    def __init__(self):
        """Construtor."""
        self.lista_produtos = LDDE()
        self.id_produto = 0

    def seta_id(self):
        """
        Define o id do produto.

        incrementa em 1 para cada mercadoria cadastrada.
        """
        self.id_produto += 1

        return self.id_produto

    def insere_produto(self, nome, preco, qtd_minima, qtd):
        """Insere produto."""
        produto = Produto(id_produto=self.seta_id(),
                          nome=nome,
                          preco=preco,
                          qtd_minima=qtd_minima,
                          qtd=qtd)

        self.lista_produtos.insere(produto)

    def remove_produto(self, id_produto):
        """Remove produto."""
        posicao = 0
        for i in self.lista_produtos:
            if id_produto == i.descricao.busca('id'):
                self.lista_produtos.remove(posicao)
            posicao += 1

    def busca_produto(self, nome_produto):
        """Busca produto por nome."""
        posicao = 0
        for i in self.lista_produtos:
            if nome_produto == i.descricao.busca('nome'):
                return self.lista_produtos.busca(posicao)
            posicao += 1

    def lista_todos_produtos(self):
        """Lista de todos os produtos."""
        return self.lista_produtos

    def gera_lista_ordenada(self):
        """Lista ordenada por prioridade(menor quantidade)."""
        lista = LES(len(self))
        for i in self.lista_produtos:
            lista.end_insert(i)

        aux = None
        for j in range(len(lista) - 1):
            for i in range(len(lista) - 1):
                if int(lista.pos_search(i).descricao.busca("qtd")) >\
                        int(lista.pos_search(i + 1).descricao.busca("qtd")):
                    aux = lista.pos_search(i)
                    lista.pos_insert(lista.pos_search(i + 1), i)
                    lista.pos_insert(aux, i + 1)

        return lista

    def __iter__(self):
        """Iterador."""
        for i in self.lista_produtos:
            yield i

    def __len__(self):
        """Retorna qtd de produtos."""
        return len(self.lista_produtos)
