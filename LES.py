"""."""


class LES:
    """."""

    def __init__(self, cap):
        """Construtor."""
        self.elements = [None] * cap
        self.size = 0
        self.cap = cap

    def end_insert(self, element):
        """Insere no final da lista."""
        if self.cap > self.size:
            self.elements[self.size] = element
            self.size += 1
            return True

        return False

    def pos_insert(self, element, position):
        """Insere em qualquer posicao da lista(permite sobreescrever)."""
        if position > self.size or position < 0:
            return False
        if self.size == self.cap:
            self.elements[position] = element
            return True
        for i in range(self.size - 1, position, -1):
            self.elements[i + 1] = self.elements[i]
        self.elements[position] = element
        self.size += 1
        return True

    def pos_remove(self, pos):
        """Remove de qualquer posicao da lista."""
        if self.size > 0 and pos >= 0 and pos < self.size:
            for i in range(pos, self.size - 1):
                self.elements[i] = self.elements[i + 1]
            self.size -= 1
            return True

        return False

    def elem_remove(self, element):
        """Remove por elemento."""
        return self.pos_remove(self.elem_search(element))

    def pos_search(self, pos):
        """Busca por posicao."""
        if pos >= self.size or pos < 0:
            return False

        return self.elements[pos]

    def elem_search(self, element):
        """Busca por elemento."""
        for i in range(self.size):
            if self.elements[i] == element:
                return i

        return -1

    def show_all(self):
        """Exibe todos."""
        for i in range(self.size):
            print(self.elements[i])

    def __iter__(self):
        """Iterador."""
        for i in range(self.size):
            yield self.elements[i]

    def __len__(self):
        """Retorna tamanho."""
        return self.size
