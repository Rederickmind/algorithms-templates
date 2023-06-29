from typing import List, Tuple


def get_sum(number_list: List[int], k: int) -> List[int]:
    number = int(''.join(map(str, number_list)))
    result = number + k
    return list(str(result))


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k


number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))
