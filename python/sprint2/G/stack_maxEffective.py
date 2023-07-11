class Stack:
    def __init__(self):
        self.main_stack = []
        self.maxes_stack = []

    def push(self, item):
        self.main_stack.append(item)
        if (len(self.maxes_stack) == 0
                or item >= self.maxes_stack[-1]):
            self.maxes_stack.append(item)

    def pop(self):
        if len(self.main_stack) != 0:
            item = self.main_stack.pop()
            if self.maxes_stack[-1] == item:
                self.maxes_stack.pop()
            return item
        return None

    def peek(self):
        return self.main_stack[-1]

    def size(self):
        return len(self.main_stack)

    def get_max(self):
        if len(self.maxes_stack) == 0:
            return None
        return self.maxes_stack[-1]


def main(commands):
    stack = Stack()
    for command in commands:
        if command[0] == 'push':
            stack.push(int(command[1]))
        if command[0] == 'pop':
            if stack.pop() is None:
                print('error')
        if command[0] == 'get_max':
            print(stack.get_max())


def read_input():
    n = int(input())
    commands = [input().strip().split() for i in range(n)]
    return commands


if __name__ == '__main__':
    main(read_input())
