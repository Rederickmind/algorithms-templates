# Successful ID in Yandex.Contest - 89113136

class NoItemsException(Exception):
    def __init__(self):
        pass


class MaxItemsException(Exception):
    def __init__(self):
        pass


class Deque:
    def __init__(self, max_length):
        self.__deque = [None] * max_length
        self.__max_length = max_length
        self.__head = -1
        self.__tail = 0
        self.__size = 0

    def push_front(self, value):
        '''Добавление элемента в начало очереди.'''
        if self.is_full():
            raise MaxItemsException
        self.__deque[self.__head] = value
        self.__size += 1
        self.__head = self.__get_index(self.__head, - 1)

    def push_back(self, value):
        '''Добавление элемента в конец очереди.'''
        if self.is_full():
            raise MaxItemsException
        self.__deque[self.__tail] = value
        self.__size += 1
        self.__tail = self.__get_index(self.__tail, 1)

    def pop_front(self):
        '''Удаление элемента из начала очереди и его вывод.'''
        if self.is_empty():
            raise NoItemsException
        self.__head = self.__get_index(self.__head, 1)
        value = self.__deque[self.__head]
        self.__size -= 1
        return value

    def pop_back(self):
        '''Удаление элемента из конца очереди и его вывод.'''
        if self.is_empty():
            raise NoItemsException
        self.__tail = self.__get_index(self.__tail, - 1)
        value = self.__deque[self.__tail]
        self.__size -= 1
        return value

    def __get_index(self, index, change):
        """Получение нового указателя, после добавления/удаления элемента."""
        return (index + change) % self.__max_length

    def size(self):
        '''Возвращение размера (длины) очереди.'''
        return self.__size

    def is_empty(self):
        '''Проверка не пустая ли очередь.'''
        return self.__size == 0

    def is_full(self):
        '''Проверка не полная ли очередь.'''
        return self.__size == self.__max_length

    def __str__(self):
        return ' '.join(map(str, self.__deque))


def main():
    command_amount = int(input())
    max_length = int(input())
    deque = Deque(max_length)
    for i in range(command_amount):
        command, *args = input().split()
        try:
            result = getattr(deque, command)(*args)
            if result is not None:
                print(result)
        except (NoItemsException, MaxItemsException):
            print('error')


if __name__ == '__main__':
    main()
