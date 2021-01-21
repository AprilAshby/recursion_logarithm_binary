# 0 1 2 3 4 5 6 7  8  9  10 11 12  ...
# 0 1 1 2 3 5 8 13 21 34 55 89 144 ...

"""
fib(0): 0
fib(1): 1
fib(n): fib(n-1) + fib(n-2)
"""


def fib_naive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_naive(n-1) + fib_naive(n-2)


cache = {}


def fib_memoized(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n not in cache:
        cache[n] = fib_memoized(n-1) + fib_memoized(n-2)
    return cache[n]


def fib_iter(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev = 0
    cur = 1

    for _ in range(n - 1):
        nxt = prev + cur
        prev = cur
        cur = nxt

    return nxt


for i in range(10):
    print(f"{i:3} {fib_iter(i)}")

# for i in range(10):
#     print(f"{i:3} {fib_memoized(i)}")

# for i in range(10):
#     print(f"{i:3} {fib_naive(i)}")
