def to_binary(number: int) -> str:
    result = ''
    if number == 0:
        result = '0'
        return result
    while number > 0:
        result = str(number % 2) + result
        number = number // 2
    return result


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
