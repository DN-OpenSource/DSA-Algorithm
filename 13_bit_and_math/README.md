# Module 13 — Bit Manipulation and Number Theory

## Theory

Computers store everything as bits. Operating directly on bits is fast and
sometimes lets you replace a loop with a single CPU instruction.

| Op           | Symbol | Meaning                                |
|--------------|--------|----------------------------------------|
| AND          | `&`    | 1 only where both inputs are 1         |
| OR           | `\|`   | 1 where either input is 1              |
| XOR          | `^`    | 1 where inputs differ                  |
| NOT          | `~`    | flip every bit                         |
| left shift   | `<<`   | multiply by 2^k                        |
| right shift  | `>>`   | divide by 2^k                          |

Useful tricks:

* `x & 1`           — is x odd?
* `x & (x - 1)`     — clears the lowest set bit (count set bits = repeat until 0)
* `x ^ x == 0`      — XOR of a value with itself is 0
* `a ^ b ^ b == a`  — XOR is its own inverse → find the unique element

## Number theory cheats

* **GCD** (Euclid): `gcd(a, b) = gcd(b, a % b)`, `gcd(a, 0) = a`.
* **Sieve of Eratosthenes**: list all primes < n in O(n log log n).
* **Modular exponentiation**: `pow(a, b, m)` in O(log b).

## Worked example: find the lonely number

Every number appears twice except one. XOR them all; pairs cancel, the
lonely number remains. `[2,3,5,3,2] -> 5`.

## Run

```
python3 dsa_course/13_bit_and_math/bit_tricks.py
python3 dsa_course/13_bit_and_math/number_theory.py
```
