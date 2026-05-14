# Module 15 — Bridge to AI

You now have the tools. AI/ML is built almost entirely from things you've
seen: arrays (called "tensors"), graphs (called "computation graphs"),
recursion (called "backpropagation"), and a *lot* of math on top.

## The picture

* Data is encoded as **vectors** of numbers.
* A **model** is a function `f(x; theta)` that maps input vectors `x` to
  output vectors `y`, parameterised by **weights** `theta`.
* A **loss function** `L(y_pred, y_true)` measures how wrong we are.
* We adjust `theta` to reduce loss — this is **learning**.
* The standard learning algorithm is **gradient descent**: move `theta` a
  tiny step in the direction that lowers the loss.

## What you'll build in this module

1. `vectors.py` — dot product, norm, cosine similarity. The "atom" of ML.
2. `linear_regression.py` — fit a line `y = wx + b` with gradient descent.
3. `knn.py` — k-Nearest-Neighbours classifier. Uses distances + sorting.
4. `kmeans.py` — unsupervised clustering. Uses distances + averaging.
5. `perceptron.py` — the simplest "neuron" that learns a linear decision boundary.
6. `neural_net.py` — a 2-layer neural net from scratch (forward pass,
   backpropagation, one optimization step) on the XOR problem.

## Why each DSA topic shows up in AI

| DSA topic        | Where it appears in AI                          |
|------------------|-------------------------------------------------|
| Arrays           | tensors, embeddings, images, audio              |
| Hash tables      | tokenizers, vocabularies, feature lookup        |
| Trees            | decision trees, random forests, XGBoost, MCTS   |
| Heaps            | top-K retrieval, beam search, priority replay   |
| Graphs           | computation graph, knowledge graphs, GNNs       |
| BFS / DFS        | search in games (chess, Go), pathfinding for robots|
| Recursion        | backpropagation                                 |
| DP               | RL value iteration, HMM Viterbi, edit distance  |
| Sorting          | ranking, top-K results                          |
| Binary search    | hyper-parameter search, retrieval, learning rate finder|
| Greedy           | greedy decoding, A* heuristics                  |
| Bit tricks       | quantized models, hashing tricks                |
| Tries            | autocomplete in search, BPE tokenizers          |
| Union-Find       | image segmentation, clustering                  |
| Segment tree     | range-sum reward in RL, fast attention variants |

## Run order

```
python3 dsa_course/15_bridge_to_ai/vectors.py
python3 dsa_course/15_bridge_to_ai/linear_regression.py
python3 dsa_course/15_bridge_to_ai/knn.py
python3 dsa_course/15_bridge_to_ai/kmeans.py
python3 dsa_course/15_bridge_to_ai/perceptron.py
python3 dsa_course/15_bridge_to_ai/neural_net.py
```

All files use **pure Python** (no NumPy) so you see every step. Once this
clicks, switching to NumPy / PyTorch is just learning the API.

## What to study next (after this course)

  1. Linear algebra (vectors, matrices, dot products, eigenvalues).
  2. Probability and statistics (Bayes, distributions, expectation).
  3. Calculus (derivatives, chain rule) — needed for backprop intuition.
  4. NumPy → PyTorch (or JAX). Re-implement these files using tensors.
  5. Andrej Karpathy's "Neural Networks: Zero to Hero" video series.
  6. Pick a real task: train a digit classifier on MNIST, fine-tune a tiny
     LLM, build a tiny RAG system over your notes. Ship something small.
