# Module 8 — Hashing and Hash Tables

## Theory

A **hash table** stores key→value pairs and lets you look them up in
*average* **O(1)** time. The trick: compute `h = hash(key) % table_size` and
use it as an index into an array of *buckets*.

Two keys can produce the same bucket → **collision**. Two ways to handle it:

* **Chaining** — each bucket holds a linked list of (k, v) pairs.
* **Open addressing** — if the bucket is full, probe the next slot.

When the table gets too full (load factor > ~0.7), we **resize** (double the
array and re-hash everything). Resizing is O(n) but amortizes to O(1) per
insert.

## Why hashes are everywhere

* Python's `dict` and `set` — hash tables.
* Database indexes (some), caches (LRU), deduplication.
* "Have I seen this before?" → set lookup.
* "Count occurrences" → dict.

## A good hash function...

  * Spreads keys uniformly across buckets.
  * Is fast to compute.
  * Is deterministic (same input → same hash).

## Worked example: two-sum (unsorted)

Given `nums = [2, 7, 11, 15]`, target = 9. Walk left to right; for each `x`
check if `target - x` was seen before. Store `x → index` in a dict.

i=0: x=2, need 7, not seen, store {2:0}.
i=1: x=7, need 2, seen at 0 → return (0, 1).

## Run

```
python3 dsa_course/08_hashing/hash_table.py
python3 dsa_course/08_hashing/hashing_patterns.py
```
