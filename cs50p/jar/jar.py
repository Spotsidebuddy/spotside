class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        text_representarion = '🍪'*self.size
        return f'{text_representarion}'

    def deposit(self, n=1):
        if self.size + n > self._capacity:
            raise ValueError('Not enough space in the jar!')
        self._size += n

    def withdraw(self, n=1):
        if self.size - n < 0:
            raise ValueError('Not enough cookies in the jar!')
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if not 0 <= size <= self._capacity:
            raise ValueError
        self._size = size
