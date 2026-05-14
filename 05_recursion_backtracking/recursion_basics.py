"""Factorial, Fibonacci (naive vs memoized), power, sum of digits."""


def factorial(n):
    if n <= 1:                # base case
        return 1
    return n * factorial(n - 1)


def fib_slow(n):              # O(2^n) -- exponential
    if n < 2:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)


def fib_fast(n, memo=None):   # O(n) with memoization
    if memo is None:
        memo = {}
    if n < 2:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_fast(n - 1, memo) + fib_fast(n - 2, memo)
    return memo[n]


def power(base, exp):
    """Fast exponentiation: O(log exp)."""
    if exp == 0:
        return 1
    half = power(base, exp // 2)
    return half * half * (base if exp % 2 else 1)


def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


if __name__ == "__main__":
    print("5! =", factorial(5))
    print("fib_slow(10) =", fib_slow(10))
    print("fib_fast(50) =", fib_fast(50))
    print("2^10 =", power(2, 10))
    print("sum_digits(12345) =", sum_digits(12345))
