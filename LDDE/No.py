"""."""


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
