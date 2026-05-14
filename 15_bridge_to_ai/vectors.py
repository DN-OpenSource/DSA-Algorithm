"""Vectors -- the foundation of every ML model.

A 'vector' is just a list of numbers. In ML it might represent:
  * an image (pixels flattened),
  * a word ('embedding'),
  * a user's preferences,
  * the parameters of a model.

We implement the operations every ML algorithm uses.
"""

import math


def add(a, b):       return [x + y for x, y in zip(a, b)]
def sub(a, b):       return [x - y for x, y in zip(a, b)]
def scale(a, k):     return [k * x for x in a]
def dot(a, b):       return sum(x * y for x, y in zip(a, b))
def norm(a):         return math.sqrt(dot(a, a))


def cosine_similarity(a, b):
    """How similar are two vectors? 1 = same direction, 0 = orthogonal."""
    return dot(a, b) / (norm(a) * norm(b))


def euclidean(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


if __name__ == "__main__":
    u = [1, 2, 3]
    v = [4, 5, 6]
    print("u + v        :", add(u, v))
    print("2u           :", scale(u, 2))
    print("dot(u, v)    :", dot(u, v))
    print("|u|          :", norm(u))
    print("cos(u, v)    :", cosine_similarity(u, v))
    print("euclid(u, v) :", euclidean(u, v))

    # Embeddings: "king" is closer to "queen" than to "banana"
    king   = [0.9, 0.8, 0.1]
    queen  = [0.85, 0.82, 0.12]
    banana = [0.1, 0.05, 0.95]
    print("cos(king, queen) :", round(cosine_similarity(king, queen), 4))
    print("cos(king, banana):", round(cosine_similarity(king, banana), 4))
