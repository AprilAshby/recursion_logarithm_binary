def searchList(n, fib_nums, L, R):
    if n == 1:
        return True
    if fib_nums[L] > fib_nums[R]:
        return False
    if fib_nums[L] + fib_nums[R] == n:
        return True
    elif fib_nums[L] + fib_nums[R] < n:
        return searchList(n, fib_nums, L + 1, R)
    elif fib_nums[L] + fib_nums[R] > n:
        return searchList(n, fib_nums, L, R - 1)


def fibList(n, first, second, fib_nums):
    if first + second < n:
        fib_nums.append(first + second)
        fibList(n, second, first + second, fib_nums)


def fibonacciSimpleSum2(n):
    fib_nums = []
    fibList(n, 0, 1, fib_nums)
    return searchList(n, fib_nums, 0, len(fib_nums) - 1)


print(fibonacciSimpleSum2(1))  # T
print(fibonacciSimpleSum2(11))  # T
print(fibonacciSimpleSum2(60))  # T
print(fibonacciSimpleSum2(66))  # F
print(fibonacciSimpleSum2(144))  # T
print(fibonacciSimpleSum2(1928372849))  # F
print(fibonacciSimpleSum2(35))  # T
print(fibonacciSimpleSum2(50))  # F
print(fibonacciSimpleSum2(70140877))  # F
