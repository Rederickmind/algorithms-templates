BUTTONS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def combinations(numbers, result='', i=0):
    if i == len(numbers):
        print(result, end=' ')
        return
    for letter in BUTTONS[numbers[i]]:
        combinations(numbers, result + letter, i + 1)


if __name__ == "__main__":
    combinations(input())
