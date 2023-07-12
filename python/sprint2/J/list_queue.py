class QueueList:
    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

        def get_value(self):
            return self.value

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get(self):
        if self.is_empty():
            return 'error'
        if self.size == 1:
            element = self.head
            self.__init__()
            return element.get_value()
        if self.size == 2:
            element = self.head
            self.head = self.tail
            self.size -= 1
            return element.get_value()
        element = self.head
        self.head = self.tail.next.next
        self.tail.next = self.head
        self.size -= 1
        return element.get_value()

    def put(self, element):
        if self.is_empty():
            self.head = self.Node(element)
            self.tail = self.head
        else:
            self.tail.next = self.Node(element)
            self.tail.next.next = self.head
            self.tail = self.tail.next
        self.size += 1

    def size(self):
        return self.size


def read_input():
    command_amount = int(input())
    commands = [input().strip().split() for i in range(command_amount)]

    return commands


def main(commands):
    queue_list = QueueList()
    for command in commands:
        if command[0] == 'put':
            queue_list.put(command[1])
        elif command[0] == 'get':
            answer = queue_list.get()
            print(answer)
        elif command[0] == 'size':
            print(queue_list.size)


if __name__ == '__main__':
    commands = read_input()
    main(commands)
