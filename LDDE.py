"""."""


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

    def busca(self, pos):
        """Busca por posicao."""
        if pos < 0:
            return -1

        elemento = self.primeiro
        for i in range(pos):
            if elemento.proximo:
                elemento = elemento.proximo
            else:
                return -1

        return elemento.conteudo

    def busca_conteudo(self, conteudo):
        """Busca por conteudo, retorna posicao."""
        if self.primeiro.conteudo == conteudo:
            return 0
        if self.ultimo.conteudo == conteudo:
            return self.tamanho - 1

        posicao = 0
        for i in self:
            if i == conteudo:
                return posicao
            posicao += 1

        return -1

    def remove(self, pos):
        """Remove por posicao."""
        if pos < 0 or pos >= self.tamanho or self.tamanho == 0:
            return False

        if pos == 0:
            self.primeiro = self.primeiro.proximo if self.tamanho > 1\
                else None
        elif pos == self.tamanho - 1:
            self.ultimo.anterior.proximo = None
            self.ultimo = self.ultimo.anterior
        else:
            elemento = self.primeiro
            for i in range(pos):
                if elemento.proximo:
                    elemento = elemento.proximo
            if elemento.proximo:
                elemento.anterior.proximo = elemento.proximo
                elemento.proximo.anterior = elemento.anterior

        self.tamanho -= 1

        return True

    def remove_conteudo(self, conteudo):
        """Remove por conteudo."""
        return self.remove(self.busca_conteudo(conteudo))

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


class No:
    """."""

    def __init__(self, conteudo=None, anterior=None, proximo=None):
        """Construtor."""
        self.conteudo = conteudo
        self.anterior = anterior
        self.proximo = proximo

    def __str__(self):
        """Usando para dar print direto no No."""
        return str(self.conteudo)
