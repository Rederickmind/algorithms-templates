# Successful ID in Yandex.Contest - 89397058

class Player:

    def __init__(self, username, tasks_solved, penalty):
        self.username = username
        self.tasks_solved = tasks_solved
        self.penalty = penalty

    def __gt__(self, other):
        if self.tasks_solved != other.tasks_solved:
            return self.tasks_solved < other.tasks_solved

        if self.penalty != other.penalty:
            return self.penalty > other.penalty

        return self.username > other.username

    def __lt__(self, other):
        if self.tasks_solved != other.tasks_solved:
            return self.tasks_solved > other.tasks_solved

        if self.penalty != other.penalty:
            return self.penalty < other.penalty

        return self.username < other.username

    def __ge__(self, other):
        return self.__gt__(other) or self == other

    def __le__(self, other):
        return self.__lt__(other) or self == other

    def __str__(self):
        return self.username


def partition(array, start, end):
    i = start - 1
    pivot = array[end]
    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1


def quick_sort_inplace(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start < end:
        pivot = partition(array, start, end)
        # сортировка нижней половины
        quick_sort_inplace(array, start, pivot - 1)
        # сортировка верхней половины
        quick_sort_inplace(array, pivot + 1, end)


def read_input():
    players_amount = int(input())
    players = [Player(username, int(tasks_solved), int(penalty))
               for _ in range(players_amount)
               for username, tasks_solved, penalty
               in [input().split()]]

    return players_amount, players


def main():
    players_amount, players = read_input()
    quick_sort_inplace(players, start=0, end=players_amount - 1)

    for player in players:
        print(player)


if __name__ == '__main__':
    main()
