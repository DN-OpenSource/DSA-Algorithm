# Module 1 — Foundations

## 1. What is a data structure? What is an algorithm?

* **Data structure** = a *way to organize data* so we can use it efficiently.
  Example: a phone book sorted alphabetically is a data structure.
* **Algorithm** = a *finite, unambiguous sequence of steps* that turns input
  into output. Example: "to find a name, open the middle page; if the name is
  earlier, look in the left half; else the right half; repeat" — that is the
  binary search algorithm.

Good software = the right data structure + the right algorithm.

## 2. Why do we care about speed? Big-O notation

Computers are fast, but inputs are huge. Doubling the input shouldn't cost
1000× more time. Big-O is a way of describing **how the runtime grows with
the input size `n`**, ignoring constants and small terms.

| Big-O      | Name         | Example                                    |
|------------|--------------|--------------------------------------------|
| O(1)       | constant     | look up array[5]                           |
| O(log n)   | logarithmic  | binary search                              |
| O(n)       | linear       | scan a list                                |
| O(n log n) | linearithmic | merge sort                                 |
| O(n^2)     | quadratic    | nested loops over the list                 |
| O(2^n)     | exponential  | brute-force subset enumeration             |
| O(n!)      | factorial    | brute-force permutations (travelling sales)|

Rule of thumb at n = 10^6:
  O(n) → milliseconds. O(n^2) → minutes. O(2^n) → universe heat-death.

## 3. Worked example

Count how many times the line marked `*` runs in this loop:

    for i in range(n):        # n iterations
        for j in range(n):    # n iterations each
            x += 1            # *

Inner line runs n × n = n^2 times → **O(n^2)**.

## 4. Space complexity

Same idea, but measuring **memory** used, not time. Recursion uses O(depth)
memory for the call stack even if it allocates no arrays.

## 5. Mental model for solving any DSA problem

  1. Re-read the problem; restate it in your own words.
  2. Write 1–2 small examples by hand.
  3. Brute force: any solution that works, even if slow. Get its Big-O.
  4. Look for the bottleneck: which step is slow? Why?
  5. Pick a data structure that removes that bottleneck.
  6. Code it, test edge cases (empty input, one element, duplicates).

Read `big_o.py` for an empirical demo, and `complexity_examples.py` for code
patterns next to their Big-O label.
