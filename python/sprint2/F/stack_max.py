class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) != 0:
            return self.items.pop()
        return None

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def get_max(self):
        if len(self.items) == 0:
            return None
        return max(self.items)


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
