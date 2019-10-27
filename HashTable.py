"""Doc."""


class HashTable:
    """."""

    def __init__(self, n=100):
        """Construtor."""
        self.hash_table = [None] * n
        self.chaves = []

    def funcao_hash(self, chave):
        """."""
        return hash(chave) % len(self.hash_table)

    def adiciona(self, chave, conteudo):
        """Adiciona."""
        if not self.hash_table[self.funcao_hash(chave)]:
            self.chaves.append(chave)
            self.hash_table[self.funcao_hash(chave)] = [[chave, conteudo]]
        else:
            if chave in self.chaves:
                for i in self.hash_table[self.funcao_hash(chave)]:
                    if i[0] == chave:
                        i[1] = conteudo
                        break
            else:
                self.chaves.append(chave)
                self.hash_table[self.funcao_hash(chave)].\
                    append([chave, conteudo])

        return self

    def busca(self, chave, padrao=None):
        """Busca."""
        if chave not in self.chaves or (
                not self.hash_table[self.funcao_hash(chave)]):
            return padrao

        for i in self.hash_table[self.funcao_hash(chave)]:
            if i[0] == chave:
                return i[1]

        return padrao

    def remove(self, chave):
        """Remove elemento por chave."""
        if chave not in self.chaves or \
                not self.hash_table[self.funcao_hash(chave)]:
            return False

        if len(self.hash_table[self.funcao_hash(chave)]) == 1:
            self.hash_table[self.funcao_hash(chave)] = None
        else:
            for i, j in enumerate(self.hash_table[self.funcao_hash(chave)]):
                if j[0] == chave:
                    self.hash_table[self.funcao_hash(chave)].pop(i)
                    break

        for i, j in enumerate(self.chaves):
            if chave == j:
                self.chaves.pop(i)

        return self

    def __iter__(self):
        """Iterador."""
        for i in [(chave, self.busca(chave)) for chave in self.chaves]:
            yield i

    def __len__(self):
        """Retorna tamanho."""
        return len(self.chaves)
