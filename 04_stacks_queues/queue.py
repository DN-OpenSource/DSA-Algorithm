"""Queue and Deque. Also: implement queue with two stacks."""

from collections import deque


class Queue:
    def __init__(self):
        self._d = deque()
    def enqueue(self, x): self._d.append(x)
    def dequeue(self):    return self._d.popleft()
    def peek(self):       return self._d[0] if self._d else None
    def __len__(self):    return len(self._d)


class QueueFromTwoStacks:
    """Classic interview: build a FIFO queue using two LIFO stacks."""
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def enqueue(self, x):
        self.inbox.append(x)

    def dequeue(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop()


if __name__ == "__main__":
    q = Queue()
    for x in [1, 2, 3]:
        q.enqueue(x)
    print("dequeue:", q.dequeue(), q.dequeue(), q.dequeue())

    q2 = QueueFromTwoStacks()
    for x in "ABCDE":
        q2.enqueue(x)
    print("two-stack q:", ''.join(q2.dequeue() for _ in range(5)))
