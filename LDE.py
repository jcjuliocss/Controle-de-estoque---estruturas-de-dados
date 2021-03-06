"""."""


class LDE:
    """."""

    def __init__(self):
        """Construtor."""
        self.tamanho = 0
        self.primeiro = None

    def insere(self, conteudo):
        """Insere no fim da lista."""
        novo = No(conteudo=conteudo)
        if self.tamanho == 0:
            self.primeiro = novo
        else:
            elemento = self.primeiro
            while elemento.proximo:
                elemento = elemento.proximo
            elemento.proximo = novo

        self.tamanho += 1

    def busca(self, pos):
        """Busca por posicao."""
        if pos < 0:
            return None

        elemento = self.primeiro
        for i in range(pos):
            if elemento.proximo:
                elemento = elemento.proximo
            else:
                return None

        return elemento.conteudo

    def remove(self, pos):
        """Deleta por posicao."""
        if pos < 0 or self.tamanho == 0 or pos >= self.tamanho:
            return False

        if pos == 0:
            self.primeiro = self.primeiro.proximo if self.tamanho > 1\
                else None
        else:
            elemento = self.primeiro
            for i in range(pos - 1):
                if elemento.proximo:
                    elemento = elemento.proximo
            if elemento.proximo.proximo:
                elemento.proximo = elemento.proximo.proximo
            else:
                elemento.proximo = None

        self.tamanho -= 1

        return True

    def __str__(self):
        """Usado para dar print na lista."""
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
        """Constroi o iterador da classe."""
        elemento = self.primeiro
        while elemento:
            yield elemento.conteudo
            elemento = elemento.proximo

    def __len__(self):
        """Retorna o tamanho da lista."""
        return self.tamanho


class No:
    """No."""

    def __init__(self, conteudo=None, proximo=None):
        """Construtor."""
        self.conteudo = conteudo
        self.proximo = proximo

    def __str__(self):
        """Usando para printar o conteudo do no."""
        return str(self.conteudo)
