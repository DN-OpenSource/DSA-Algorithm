# Module 5 — Recursion and Backtracking

## Theory

A **recursive function** calls itself with a *smaller* version of the same
problem until it hits a **base case**.

Three things every recursion needs:

  1. **Base case** — when do we stop?
  2. **Recursive case** — how do we make the problem smaller?
  3. **Combine** — how do we use the smaller answer to build ours?

If you forget the base case, you blow the call stack.

## Mental model

Imagine a stack of identical copies of yourself, each one slightly lazier
than the one above. The top one says "I'll solve this if you (the one
below me) solve a smaller version first."

## Backtracking

Backtracking = recursion + "undo". You make a choice, recurse, and if it
didn't pan out, undo the choice and try the next one. Classic problems:
permutations, subsets, N-Queens, Sudoku.

Template:

```
def solve(state):
    if is_solution(state):
        record(state)
        return
    for choice in choices(state):
        if is_valid(choice, state):
            apply(choice, state)
            solve(state)
            undo(choice, state)        # the "back" of backtracking
```

## Worked example: factorial

`n! = n * (n-1)!`, base: `0! = 1`.
`3! = 3 * 2! = 3 * 2 * 1! = 3 * 2 * 1 * 0! = 3 * 2 * 1 * 1 = 6`.

## Run

```
python3 dsa_course/05_recursion_backtracking/recursion_basics.py
python3 dsa_course/05_recursion_backtracking/backtracking.py
```
