"""."""
from No import No


class LDDE:
    """."""

    def __init__(self):
        """Construtor."""
        self.tamanho = 0
        self.primeiro = None
        self.ultimo = None

    def insere(self, conteudo):
        """Insere no fim."""
        novo = No(conteudo=conteudo)
        if self.tamanho == 0:
            self.primeiro = novo
            self.ultimo = novo
        else:
            novo.anterior = self.ultimo
            self.ultimo.proximo = novo
            self.ultimo = novo

        self.tamanho += 1

    def __str__(self):
        """Permite o print direto na instancia da lista."""
        elemento = self.primeiro
        str_lista = '['
        while elemento:
            str_lista += str(elemento.conteudo)
            if elemento.proximo:
                str_lista += ', '
            elemento = elemento.proximo
        str_lista += ']'

        return str(str_lista)

    def __iter__(self):
        """Iterador."""
        elemento = self.primeiro
        while elemento:
            yield elemento.conteudo
            elemento = elemento.proximo

    def __len__(self):
        """Tamanho da lista."""
        return self.tamanho
