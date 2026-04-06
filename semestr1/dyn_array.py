class DynArray:


    def __init__(self, initial_capacity=2):
        if initial_capacity <= 0:
            raise ValueError("Initial capacity must be greater than 0")

        self._capacity = initial_capacity
        self._size = 0
        self._data = [None] * self._capacity


    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        i = 0
        while i < self._size:
            new_data[i] = self._data[i]
            i += 1

        self._data = new_data
        self._capacity = new_capacity

    def append(self, value):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)

        self._data[self._size] = value
        self._size += 1

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        return self._data[index]

    def set(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        self._data[index] = value

    def insert(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")

        if self._size == self._capacity:
            self._resize(self._capacity * 2)

        i = self._size
        while i > index:
            self._data[i] = self._data[i - 1]
            i -= 1

        self._data[index] = value
        self._size += 1

    def remove_at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")

        removed_value = self._data[index]

        i = index
        while i < self._size - 1:
            self._data[i] = self._data[i + 1]
            i += 1

        self._data[self._size - 1] = None
        self._size -= 1

        return removed_value

    def size(self):
        return self._size

    def capacity(self):
        return self._capacity

    def __str__(self):
        result = "["
        i = 0
        while i < self._size:
            result += str(self._data[i])
            if i != self._size - 1:
                result += ", "
            i += 1
        result += "]"
        return result
