def read_input():
    amount = int(input())
    clothes = input().split()
    return amount, clothes


def countsort_clothes(clothes):
    COLORS = {
        '0': 0,
        '1': 0,
        '2': 0
    }
    for cloth in clothes:
        COLORS[cloth] += 1
    result = '0 ' * COLORS['0'] + '1 ' * COLORS['1'] + '2 ' * COLORS['2']
    return result


def main():
    amount, clothes = read_input()
    print(countsort_clothes(clothes))


if __name__ == '__main__':
    main()
