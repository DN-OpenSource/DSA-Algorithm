# Module 11 — Dynamic Programming (DP)

## Theory

DP is recursion + a notebook. We solve a problem by combining solutions to
**overlapping subproblems**, and we store each subproblem's answer the
first time we compute it so we never redo work.

A problem is a DP candidate when it has:

  1. **Optimal substructure** — the optimal answer for size n can be built
     from optimal answers of smaller sizes.
  2. **Overlapping subproblems** — the same subproblem is asked many times.

Two flavours:

* **Top-down (memoization)** — recurse, cache results in a dict.
* **Bottom-up (tabulation)** — fill an array from size 0 upward.

## Three-step recipe

  1. Define the *state*: what does `dp[i]` mean? In words, in one sentence.
  2. Write the *transition*: how is `dp[i]` built from earlier states?
  3. Set the *base case* and the *answer*.

## Classic problems we cover

* Fibonacci (toy example)
* Climbing stairs
* House robber (cannot rob adjacent houses)
* Coin change (fewest coins to make amount)
* Longest common subsequence (LCS) (foundation of `diff`)
* 0/1 Knapsack

## Worked example: climbing stairs

Each step climb 1 or 2. How many distinct ways to reach step n?
`dp[n] = dp[n-1] + dp[n-2]` (came from one step below, or two below).
Base: `dp[0]=1, dp[1]=1`.

## Run

```
python3 dsa_course/11_dynamic_programming/dp_basics.py
python3 dsa_course/11_dynamic_programming/coin_change.py
python3 dsa_course/11_dynamic_programming/lcs.py
python3 dsa_course/11_dynamic_programming/knapsack.py
```
