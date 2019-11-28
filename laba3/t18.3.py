def fib(i):
    if i < 3:
        return 1
    return fib(i - 1) + fib(i - 2)


def golden_ratio(i):
    res = fib(i + 1) / fib(i)
    return res


print(golden_ratio(int(input('i = '))))
