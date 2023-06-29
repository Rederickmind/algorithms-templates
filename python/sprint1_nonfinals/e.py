def get_longest_word(line: str) -> str:
    words = line.split()
    max_length = len(words)
    long_word = words[0]
    for i in range(1, max_length):
        if len(words[i]) > len(long_word):
            long_word = words[i]
    return long_word


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
