from typing import List


def factorize(number: int) -> List[int]:
    index = 2
    result = []
    while index * index <= number:
        while number % index == 0:
            result.append(index)
            number = int(number / index)
        index += 1
    if number > 1:
        result.append(number)
    return result


result = factorize(int(input()))
print(" ".join(map(str, result)))
