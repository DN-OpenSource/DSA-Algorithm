"""Singly linked list with classic operations + reverse + cycle detection."""


class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, v):
        self.head = Node(v, self.head)

    def push_back(self, v):
        if self.head is None:
            self.head = Node(v)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(v)

    def find(self, v):
        cur = self.head
        while cur:
            if cur.value == v:
                return cur
            cur = cur.next
        return None

    def remove(self, v):
        dummy = Node(None, self.head)
        cur = dummy
        while cur.next:
            if cur.next.value == v:
                cur.next = cur.next.next
                self.head = dummy.next
                return True
            cur = cur.next
        return False

    def reverse(self):
        prev, cur = None, self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def has_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    def to_list(self):
        out, cur = [], self.head
        while cur:
            out.append(cur.value)
            cur = cur.next
        return out


if __name__ == "__main__":
    ll = SinglyLinkedList()
    for x in [3, 2, 1]:
        ll.push_front(x)
    for x in [4, 5]:
        ll.push_back(x)
    print("list :", ll.to_list())
    print("mid  :", ll.middle().value)
    ll.reverse()
    print("rev  :", ll.to_list())
    ll.remove(3)
    print("rm 3 :", ll.to_list())

    a = Node(1); b = Node(2); c = Node(3)
    a.next = b; b.next = c; c.next = a   # cycle
    tmp = SinglyLinkedList()
    tmp.head = a
    print("cycle:", tmp.has_cycle())
