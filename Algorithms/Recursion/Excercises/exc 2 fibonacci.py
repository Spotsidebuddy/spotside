def recursive_fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(recursive_fib(8))