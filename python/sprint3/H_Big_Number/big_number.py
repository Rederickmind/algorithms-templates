def comporator(num_1, num_2):
    if len(num_1) == len(num_2):
        return num_1 > num_2
    var_1 = num_1 + num_2
    var_2 = num_2 + num_1
    return var_1 > var_2


def max_num(numbers):
    for i in range(1, len(numbers)):
        item_for_sort = numbers[i]
        while i > 0 and comporator(item_for_sort, numbers[i - 1]):
            numbers[i] = numbers[i - 1]
            i -= 1
        numbers[i] = item_for_sort
    return ''.join(numbers)


if __name__ == "__main__":
    n = int(input())
    task_numbers = input().split()
    print(max_num(task_numbers))
