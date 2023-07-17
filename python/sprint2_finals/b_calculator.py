# Successful ID in Yandex.Contest - 89112878

# Операторы вычислений и функции для расчетов.
OPERATORS = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y
}


class Stack:
    def __init__(self):
        self.__data = []
        self.__size = 0

    def size(self):
        '''Возвращает размер стека.'''
        return self.__size

    def is_empty(self):
        '''Проверка не пустой ли стек.'''
        return self.__size == 0

    def push(self, element):
        '''Добавление элемента в стек.'''
        self.__data.append(element)
        self.__size += 1

    def pop(self):
        '''Получение элемента стека для расчетов или вывода результата.'''
        if self.is_empty():
            raise IndexError('Стек пустой')
        self.__size -= 1
        return self.__data.pop()


def main():
    expression = input().split()
    stack = Stack()
    for i in expression:
        if i in OPERATORS:
            operand_1, operand_2 = stack.pop(), stack.pop()
            stack.push(OPERATORS[i](operand_2, operand_1))
        else:
            stack.push(int(i))
    return stack.pop()


if __name__ == '__main__':
    print(main())
