"""Monotonic stack — find next greater element in O(n)."""


def next_greater(arr):
    """For each i, the next index j>i where arr[j] > arr[i], else -1."""
    result = [-1] * len(arr)
    stack = []                                 # indices, values decreasing
    for i, x in enumerate(arr):
        while stack and arr[stack[-1]] < x:
            result[stack.pop()] = i
        stack.append(i)
    return result


def daily_temperatures(temps):
    """How many days until a warmer day? Same monotonic-stack idea."""
    n = len(temps)
    ans = [0] * n
    st = []
    for i, t in enumerate(temps):
        while st and temps[st[-1]] < t:
            j = st.pop()
            ans[j] = i - j
        st.append(i)
    return ans


if __name__ == "__main__":
    print("next_greater:", next_greater([2, 1, 3, 4, 2, 5]))
    print("daily_temps :", daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
