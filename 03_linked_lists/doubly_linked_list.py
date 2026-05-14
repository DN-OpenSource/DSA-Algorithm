"""Doubly linked list with O(1) push/pop at either end."""


class DNode:
    __slots__ = ("v", "prev", "next")

    def __init__(self, v):
        self.v = v
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_back(self, v):
        n = DNode(v)
        if self.tail is None:
            self.head = self.tail = n
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n
        self.size += 1

    def push_front(self, v):
        n = DNode(v)
        if self.head is None:
            self.head = self.tail = n
        else:
            n.next = self.head
            self.head.prev = n
            self.head = n
        self.size += 1

    def pop_front(self):
        if self.head is None:
            return None
        n = self.head
        self.head = n.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return n.v

    def pop_back(self):
        if self.tail is None:
            return None
        n = self.tail
        self.tail = n.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return n.v

    def to_list(self):
        out, cur = [], self.head
        while cur:
            out.append(cur.v)
            cur = cur.next
        return out


if __name__ == "__main__":
    d = DoublyLinkedList()
    for x in [1, 2, 3]:
        d.push_back(x)
    d.push_front(0)
    print("dll:", d.to_list())          # [0,1,2,3]
    print("pop_back:", d.pop_back())
    print("pop_front:", d.pop_front())
    print("after:", d.to_list())
