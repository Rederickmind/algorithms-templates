from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    chaos = 0
    max_length = len(temperatures)
    if max_length == 1:
        chaos += 1
        return chaos
    # Проверяем первый элемент
    if temperatures[0] > temperatures[1]:
        chaos += 1
    # Проверяем последний элемент
    if temperatures[-1] > temperatures[-2]:
        chaos += 1
    for i in range(1, max_length - 1):
        if temperatures[i - 1] < temperatures[i] > temperatures[i + 1]:
            chaos += 1
    return chaos


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
