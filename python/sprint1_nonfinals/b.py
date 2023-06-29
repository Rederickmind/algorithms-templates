def check_parity(a: int, b: int, c: int) -> bool:
    par_a = a % 2
    par_b = b % 2
    par_c = c % 2
    if (par_a + par_b + par_c) == 0 or (par_a + par_b + par_c) == 3:
        return True
    return False


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
