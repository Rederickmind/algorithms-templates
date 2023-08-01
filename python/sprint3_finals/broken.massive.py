# Successful ID in Yandex.Contest - 89397129

def broken_search(numbers, target, left=0, right=None):
    if right is None:
        right = len(numbers) - 1
    if left > right:
        return -1
    middle = (left + right) // 2
    if target == numbers[middle]:
        return middle

    if numbers[left] <= numbers[middle]:
        if numbers[left] <= target <= numbers[middle]:
            return broken_search(numbers, target, left, middle - 1)
        return broken_search(numbers, target, middle + 1, right)
    if numbers[middle] <= target <= numbers[right]:
        return broken_search(numbers, target, middle + 1, right)
    return broken_search(numbers, target, left, middle - 1)


def read_input():
    array_length = int(input())
    target = int(input())
    numbers = [int(num) for num in input().split()]
    return numbers, target


def main():
    numbers, target = read_input()
    print(broken_search(numbers, target))


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


if __name__ == '__main__':
    main()
