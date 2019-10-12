"""Docstring da classe produto."""

class Produto:
	def __init__(self, nome, qtd_minima, qtd_inicial = 0):
		"""Construtor."""
		self.nome = nome
		self.qtd_minima = qtd_minima
		self.qtd_inicial = qtd_inicial
