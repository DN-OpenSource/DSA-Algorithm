# Module 3 — Linked Lists

## Theory

A **linked list** is a chain of `Node` objects. Each node holds a `value` and
a pointer to the `next` node. The list is identified by a pointer to its
`head`.

Compared to an array:

| Operation               | Array  | Linked list (single) |
|-------------------------|--------|----------------------|
| Random access `[i]`     | O(1)   | O(n)                 |
| Insert at head          | O(n)   | O(1)                 |
| Insert at tail          | O(1)*  | O(n) (or O(1) if you keep a tail pointer) |
| Delete given a node ptr | O(n)   | O(1)                 |
| Memory locality         | great  | poor (pointer chasing)|

**Variants:**

* **Singly linked**: each node knows only its `next`.
* **Doubly linked**: each node knows both `next` and `prev` (faster delete).
* **Circular**: the last node's `next` points back to head.

## Two famous patterns

* **Fast & slow pointers (tortoise & hare)** — detect cycles, find middle.
* **Reverse a linked list** — three pointers: `prev`, `curr`, `next`.

## Worked example: reverse a list

List: 1 → 2 → 3 → None.
Start: prev=None, curr=1.
Iteration 1: nxt=2; curr.next = prev (None); prev=1; curr=2.
Iteration 2: nxt=3; curr.next = prev (1); prev=2; curr=3.
Iteration 3: nxt=None; curr.next = prev (2); prev=3; curr=None. Done.
Result: 3 → 2 → 1 → None.

## Run

```
python3 dsa_course/03_linked_lists/singly_linked_list.py
python3 dsa_course/03_linked_lists/doubly_linked_list.py
```
