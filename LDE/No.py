"""."""


class No:
    """No."""

    def __init__(self, conteudo=None, proximo=None):
        """Construtor."""
        self.conteudo = conteudo
        self.proximo = proximo

    def __str__(self):
        """Usando para printar o conteudo do no."""
        return str(self.conteudo)
