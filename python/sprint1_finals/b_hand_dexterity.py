# Successful ID in Yandex.Contest - 88733622

from collections import Counter


def read_input():
    k = int(input())
    # Считываем 4 строки матрицы в одну
    keyboard = ''.join(input() for _ in range(4)).replace('.', '')
    # Создаём словарь количества вхождений числа в клавиатуру для раунда
    key_counter = dict(Counter(keyboard))

    return key_counter, k


def score_count(key_counter, k):
    score = 0
    # В цикле проверяем количество кнопок соответствующих раунду
    # и могут ли их нажать два игрока
    for i in range(1, 10):
        if str(i) in key_counter.keys():
            if 0 < key_counter[str(i)] <= 2*k:
                score += 1
    return score


def main():
    key_counter, k = read_input()
    print(score_count(key_counter, k))


if __name__ == '__main__':
    main()
