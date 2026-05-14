"""Stack + classic uses: balanced parens, reverse polish notation."""


class Stack:
    def __init__(self):
        self._data = []

    def push(self, x):   self._data.append(x)
    def pop(self):       return self._data.pop() if self._data else None
    def peek(self):      return self._data[-1] if self._data else None
    def is_empty(self):  return not self._data
    def __len__(self):   return len(self._data)


def balanced(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    st = Stack()
    for c in s:
        if c in '([{':
            st.push(c)
        elif c in ')]}':
            if len(st) == 0 or st.pop() != pairs[c]:
                return False
    return len(st) == 0


def eval_rpn(tokens):
    """Reverse Polish Notation: '3 4 +' -> 7. tokens is a list."""
    st = Stack()
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b),
    }
    for t in tokens:
        if t in ops:
            b = st.pop(); a = st.pop()
            st.push(ops[t](a, b))
        else:
            st.push(int(t))
    return st.pop()


if __name__ == "__main__":
    print("balanced ([]{}):", balanced("([]{})"))
    print("balanced (]    :", balanced("(]"))
    print("rpn 3 4 + 2 *  :", eval_rpn(['3', '4', '+', '2', '*']))
