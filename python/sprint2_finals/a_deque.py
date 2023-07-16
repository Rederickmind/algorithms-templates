class NoItemsException(Exception):
    def __init__(self):
        pass


class MaxItemsException(Exception):
    def __init__(self):
        pass


class Deque:
    def __init__(self, max_length):
        self.deque = [None] * max_length
        self.max_length = max_length
        self.head = 0
        self.tail = 0
        self.size = 0

    def push_front(self, value):
        '''Добавление элемента в начало очереди.'''
        if self.is_full():
            raise MaxItemsException
        self.head = self.get_index('push_front')
        self.deque[self.head] = value
        self.size += 1

    def push_back(self, value):
        '''Добавление элемента в конец очереди.'''
        if self.is_full():
            raise MaxItemsException
        self.tail = self.get_index('push_back')
        self.deque[self.tail] = value
        self.size += 1

    def pop_front(self):
        '''Удаление элемента из начала очереди и его вывод.'''
        if self.is_empty():
            raise NoItemsException
        value = self.deque[self.head]
        self.head = self.get_index('pop_front')
        self.size -= 1
        return value

    def pop_back(self):
        '''Удаление элемента из конца очереди и его вывод.'''
        if self.is_empty():
            raise NoItemsException
        value = self.deque[self.tail]
        self.tail = self.get_index('pop_back')
        self.size -= 1
        return value

    def get_index(self, method):
        """Получение нового указателя, после добавления/удаления элемента."""
        if method == 'push_front':
            if self.is_empty():
                self.head = 0
                self.tail = 0
                return 0
            return (self.head - 1) % self.max_length
        if method == 'push_back':
            if self.is_empty():
                self.head = 0
                self.tail = 0
                return 0
            return (self.tail + 1) % self.max_length
        if method == 'pop_front':
            return (self.head + 1) % self.max_length
        if method == 'pop_back':
            return (self.tail - 1) % self.max_length

    def size(self):
        '''Возвращение размера (длины) очереди.'''
        return self.size

    def is_empty(self):
        '''Проверка не пустая ли очередь.'''
        return self.size == 0

    def is_full(self):
        '''Проверка не полная ли очередь.'''
        return self.size == self.max_length

    def __str__(self):
        return ' '.join(map(str, self.deque))


def main():
    command_amount = int(input())
    max_length = int(input())
    deque = Deque(max_length)

    for i in range(command_amount):
        try:
            command = input().split()
            if len(command) == 1:
                print(getattr(deque, command[0])())
            else:
                getattr(deque, command[0])(command[1])
        except NoItemsException:
            print('error')
        except MaxItemsException:
            print('error')


if __name__ == '__main__':
    main()
