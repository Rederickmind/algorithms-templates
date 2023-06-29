from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    result = list(longer)
    for c in shorter:
        if c in longer:
            result.remove(c)
    return ''.join(result)


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
