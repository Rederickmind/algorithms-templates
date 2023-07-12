class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def push(self, element):
        if self.size != self.max_size:
            self.queue[self.tail] = element
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
            return 'OK'
        return 'error'

    def pop(self):
        if self.is_empty():
            return None
        element = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return element

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size


def read_input():
    command_amount = int(input())
    max_size = int(input())
    commands = [input().strip().split() for i in range(command_amount)]

    return max_size, commands


def main(max_size, commands):
    queue = MyQueueSized(max_size)
    for command in commands:
        if command[0] == 'push':
            answer = queue.push(command[1])
            if answer == 'error':
                print(answer)
        elif command[0] == 'pop':
            print(queue.pop())
        elif command[0] == 'peek':
            print(queue.peek())
        elif command[0] == 'size':
            print(queue.size)


if __name__ == '__main__':
    max_size, commands = read_input()
    main(max_size, commands)
