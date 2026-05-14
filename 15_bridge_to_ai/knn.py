"""k-Nearest Neighbours classifier.

Idea: to classify a new point, find the k closest training points and let
them vote. No training at all -- just stored data + distances + sorting
(which you implemented in module 6!).
"""

import math
from collections import Counter


def euclidean(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def knn_predict(train_X, train_y, query, k=3):
    distances = [(euclidean(x, query), label) for x, label in zip(train_X, train_y)]
    distances.sort(key=lambda t: t[0])
    top_k = [label for _, label in distances[:k]]
    return Counter(top_k).most_common(1)[0][0]


if __name__ == "__main__":
    # Two clusters: 'cat' near (0,0), 'dog' near (10,10).
    X = [
        [0, 0], [1, 0], [0, 1], [1, 1],          # cats
        [10, 10], [9, 10], [10, 9], [11, 11],    # dogs
    ]
    y = ['cat'] * 4 + ['dog'] * 4

    for q in [[0.5, 0.5], [9.5, 9.5], [5, 5]]:
        print(f"query {q} -> {knn_predict(X, y, q, k=3)}")
