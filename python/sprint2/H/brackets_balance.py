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


def is_correct_bracket_seq(seq):
    stack = Stack()
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    for char in seq:
        if char in brackets:
            stack.push(char)
        else:
            if (stack.size() == 0 or char != brackets[stack.pop()]):
                return False
    if (stack.size() == 0):
        return True
    return False


def main():
    seq = input()
    print(is_correct_bracket_seq(seq))


if __name__ == '__main__':
    main()
