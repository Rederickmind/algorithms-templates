# Successful ID in Yandex.Contest - 88682993

MAX_LENGTH = 10 ** 6
MAX_NUM = 10 ** 9


def nearest_zero(length, houses):
    result = [0] * length
    left_zero = 0

    if max(houses) > MAX_NUM:
        return None
    if length > MAX_LENGTH:
        return None

    # Ищем первый 0 слева направо
    while houses[left_zero] != 0:
        left_zero += 1

    for i in range(left_zero, length):
        if houses[i] == 0:
            result[i] = 0
        else:
            result[i] = result[i-1] + 1

    # Ищем правый ноль справа налево
    right_zero = length - 1
    while houses[right_zero] != 0:
        right_zero -= 1

    for i in range(right_zero, left_zero, -1):
        if houses[i] == 0:
            result[i] = 0
        else:
            result[i] = min(result[i], result[i+1] + 1)

    # Заполняем левую часть до первого нуля
    for i in range(left_zero - 1, -1, -1):
        result[i] = result[i+1] + 1

    return result


length = int(input())
houses = [int(house) for house in input().strip().split()]
print(" ".join(map(str, nearest_zero(length, houses))))
