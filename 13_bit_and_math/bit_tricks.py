"""Classic bit-manipulation tricks."""


def is_power_of_two(x):
    return x > 0 and (x & (x - 1)) == 0


def count_set_bits(x):
    c = 0
    while x:
        x &= x - 1                # clears lowest set bit
        c += 1
    return c


def single_number(arr):
    r = 0
    for x in arr:
        r ^= x
    return r


def get_bit(x, i):    return (x >> i) & 1
def set_bit(x, i):    return x | (1 << i)
def clear_bit(x, i):  return x & ~(1 << i)
def toggle_bit(x, i): return x ^ (1 << i)


if __name__ == "__main__":
    print("is_power_of_two(64):", is_power_of_two(64))
    print("count_set_bits(0b10110):", count_set_bits(0b10110))
    print("single_number:", single_number([2, 3, 5, 3, 2]))
    print("set_bit(0, 3):", bin(set_bit(0, 3)))
