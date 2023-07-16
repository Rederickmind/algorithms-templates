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
            print('error')
        self.deque[self.head] = value
        # print(f'Добавили в начало элемент {self.deque[self.head]}')
        self.size += 1
        # print(f'Размер очереди теперь {self.size}')
        self.head = self.change_index(self.head, -1)

    def push_back(self, value):
        '''Добавление элемента в конец очереди.'''
        if self.is_full():
            print('error')
        self.deque[self.tail] = value
        # print(f'Добавили в конец элемент {self.deque[self.tail]}')
        self.size += 1
        # print(f'Размер очереди теперь {self.size}')
        self.tail = self.change_index(self.tail, 1)

    def pop_front(self):
        '''Удаление элемента из начала очереди и его вывод.'''
        if self.is_empty():
            return 'error'
        else:
            value = self.deque[self.head]
            self.deque[self.head] = None
            self.head = self.change_index(self.head, 1)
            self.size -= 1
            return value

    def pop_back(self):
        '''Удаление элемента из конца очереди и его вывод.'''
        # print(f'размер очереди {self.size}')
        if self.is_empty():
            return 'error'
        else:
            value = self.deque[self.tail]
            # print(f'Возвращаемый элемент {value}')
            self.deque[self.tail] = None
            self.tail = self.change_index(self.tail, -1)
            self.size -= 1
            return value

    def change_index(self, index, new_index):
        """Получение нового указателя, после добавления/удаления элемента."""
        return (index + new_index) % self.max_length

    def size(self):
        '''Возвращение размера (длины) очереди.'''
        return self.size

    def is_empty(self):
        '''Проверка не пустая ли очередь.'''
        return (self.size == 0)

    def is_full(self):
        '''Проверка не полная ли очередь.'''
        return self.size >= self.max_length


def read_input():
    '''
    Чтение данных.
    Возвращает максимальную длину очереди и команды работы с ней.
    '''
    command_amount = int(input())
    max_length = int(input())
    commands = [input().strip().split() for i in range(command_amount)]

    return max_length, commands


def main(max_length, commands):
    deque = Deque(max_length)
    for command in commands:
        if command[0] == 'push_front':
            deque.push_front(int(command[1]))
        if command[0] == 'push_back':
            deque.push_back(int(command[1]))
        if command[0] == 'pop_front':
            print(deque.pop_front())
        if command[0] == 'pop_back':
            print(deque.pop_back())


if __name__ == '__main__':
    max_length, commands = read_input()
    main(max_length, commands)
