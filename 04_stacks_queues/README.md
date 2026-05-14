# Module 4 — Stacks and Queues

## Theory

* **Stack** — LIFO (Last In, First Out). Like a stack of plates.
  Operations: `push`, `pop`, `peek`. All O(1).
* **Queue** — FIFO (First In, First Out). Like a line at the bakery.
  Operations: `enqueue`, `dequeue`, `peek`. All O(1).
* **Deque** (double-ended queue) — push/pop at either end. O(1).

## Where do they show up?

* Function calls use a **call stack** (this is why deep recursion crashes).
* Browser back/forward buttons → two stacks.
* Undo/redo → two stacks.
* Print spoolers and task schedulers → queues.
* BFS uses a queue; DFS uses a stack (or recursion).

## Monotonic stack (a power-tool pattern)

A stack whose values are always increasing (or always decreasing) as you go
top-to-bottom. Used to answer "next greater element" in O(n).

## Worked example: balanced parentheses

For each character, if it is opening `(`, `[`, `{`, push it. If it is
closing, pop and check that it matches. At the end, the stack must be empty.

`([]{})` — push `(`, push `[`, see `]` pop `[` match, see `{` push, see `}`
pop match, see `)` pop match. Stack empty → balanced.

## Run

```
python3 dsa_course/04_stacks_queues/stack.py
python3 dsa_course/04_stacks_queues/queue.py
python3 dsa_course/04_stacks_queues/monotonic_stack.py
```
