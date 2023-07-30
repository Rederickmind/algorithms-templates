def subsequence_exists(s, t):
    if len(s) == 0:
        return True

    if len(s) > len(t):
        return False

    i = 0
    for j in range(len(t)):
        if s[i] == t[j]:
            i += 1
            if i == len(s):
                return True

    return False


def read_input():
    s = input()
    t = input()
    return s, t


def main():
    s, t = read_input()
    print(subsequence_exists(s, t))


if __name__ == '__main__':
    main()
