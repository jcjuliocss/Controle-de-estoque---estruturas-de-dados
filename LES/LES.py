class LES:

    def __init__(self, cap):
        self.elements = [None] * cap
        self.size = 0
        self.cap = cap

    def end_insert(self, element):
        if self.cap > self.size:
            self.elements[self.size] = element
            self.size += 1
            return True

        return False

    def pos_insert(self, element, position):
        if position > self.size or position < 0:
            return False
        if self.cap > self.size:
            for i in range(self.size - 1, position - 1, -1):
                self.elements[i + 1] = self.elements[i]
            self.elements[position] = element
            self.size += 1
            return True

        return False

    def pos_remove(self, pos):
        if self.size > 0 and pos >= 0 and pos < self.size:
            for i in range(pos, self.size):
                self.elements[i] = self.elements[i + 1]
            self.size -= 1
            return True

        return False

    def elem_remove(self, element):
        return self.pos_remove(self.elem_search(element))

    def pos_search(self, pos):
        if pos >= self.size or pos < 0:
            return False

        return self.elements[pos]

    def elem_search(self, element):
        for i in range(self.size):
            if self.elements[i] == element:
                return i

        return -1

    def show_all(self):
        for i in range(self.size):
            print(self.elements[i])
