def bubble_sort(length, numbers):
    somethingWasChanged = False

    while True:
        somethingChanged = False
        for i in range(length-1):
            if int(numbers[i]) > int(numbers[i+1]):
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                somethingChanged = True
                somethingWasChanged = True

        if somethingChanged:
            print(' '.join(numbers))
        else:
            break

    if not somethingWasChanged:
        print(' '.join(numbers))


def main():
    length = int(input())
    numbers = input().strip().split()
    bubble_sort(length, numbers)


if __name__ == '__main__':
    main()
