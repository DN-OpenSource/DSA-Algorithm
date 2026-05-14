"""GCD, sieve of Eratosthenes, modular exponentiation."""


def is_prime(n):
    """O(sqrt n) primality test."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a // gcd(a, b) * b


def sieve(n):
    """Primes <= n."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i, p in enumerate(is_prime) if p]


def mod_pow(base, exp, mod):
    """Compute (base^exp) mod m in O(log exp)."""
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = result * base % mod
        base = base * base % mod
        exp >>= 1
    return result


if __name__ == "__main__":
    print("is_prime(17):", is_prime(17), " is_prime(18):", is_prime(18))
    print("gcd(48, 18):", gcd(48, 18))
    print("lcm(4, 6):", lcm(4, 6))
    print("primes <= 30:", sieve(30))
    print("3^200 mod 50:", mod_pow(3, 200, 50))
