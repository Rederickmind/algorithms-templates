# Successful ID in Yandex.Contest - 89088301

class NoItemsException(Exception):
    def __init__(self):
        pass


class ZeroDivisionErrorException(Exception):
    def __init__(self):
        pass


# Операторы вычислений и функции для расчетов.
OPERATORS = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y
}


class Stack:
    def __init__(self):
        self.data = []
        self.size = 0

    def size(self):
        '''Возвращает размер стека.'''
        return self.size

    def is_empty(self):
        '''Проверка не пустой ли стек.'''
        return self.size == 0

    def push(self, element):
        '''Добавление элемента в стек.'''
        self.data.append(element)
        self.size += 1

    def pop(self):
        '''Получение элемента стека для расчетов или вывода результата.'''
        if self.is_empty():
            raise NoItemsException('Стек пустой')
        self.size -= 1
        return self.data.pop()


def main():
    expression = input().split()
    stack = Stack()
    for i in expression:
        if i in OPERATORS:
            if OPERATORS[i] == '/':
                operand_1, operand_2 = stack.pop(), stack.pop()
                if operand_2 == 0:
                    raise ZeroDivisionErrorException('Нельзя делить на ноль!')
                stack.push(OPERATORS[i](operand_2, operand_1))
            operand_1, operand_2 = stack.pop(), stack.pop()
            stack.push(OPERATORS[i](operand_2, operand_1))
        else:
            stack.push(int(i))
    return stack.pop()


if __name__ == '__main__':
    print(main())
