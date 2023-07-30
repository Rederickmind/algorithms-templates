def gen_binary(n, opens, result):
    if n == opens == 0:
        print(result)

    if n == 0:
        return

    gen_binary(n-1, opens+1, result + '(')
    if opens > 0:
        gen_binary(n-1, opens-1, result + ')')


n = int(input())

gen_binary(2*n, 0, '')
