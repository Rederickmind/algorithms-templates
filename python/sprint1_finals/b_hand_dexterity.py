# Successful ID in Yandex.Contest - 88700288

def read_input():
    k = int(input())
    keyboard = ''
    # Считываем 4 строки матрицы в одну
    for i in range(4):
        keyboard = keyboard + ''.join(input()).replace('.', '')

    # Переводим строку в список, чтобы удобнее было считать вхождения
    numbers = []
    for symbol in keyboard:
        numbers.append(int(symbol))
    return numbers, k


def score_count(numbers, k):
    score = 0
    # В цикле считаем количество кнопок соответствующих раунду
    # и могут ли их нажать два игрока
    for i in range(1, 10):
        count = numbers.count(i)
        if 0 < count <= 2*k:
            score += 1
    return score


numbers, k = read_input()
print(score_count(numbers, k))
