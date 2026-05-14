"""k-Means clustering: unsupervised.
Iterate:
  1. assign each point to its nearest centroid
  2. move each centroid to the mean of its assigned points
Stop when no point changes cluster.
"""

import math
import random


def euclidean(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def mean(points):
    d = len(points[0])
    return [sum(p[i] for p in points) / len(points) for i in range(d)]


def kmeans(X, k, iters=20, seed=0):
    random.seed(seed)
    centroids = random.sample(X, k)
    for _ in range(iters):
        clusters = [[] for _ in range(k)]
        labels = []
        for p in X:
            i = min(range(k), key=lambda c: euclidean(p, centroids[c]))
            labels.append(i)
            clusters[i].append(p)
        new_centroids = [mean(c) if c else centroids[i] for i, c in enumerate(clusters)]
        if new_centroids == centroids:
            break
        centroids = new_centroids
    return labels, centroids


if __name__ == "__main__":
    X = [[0,0], [1,0], [0,1], [1,1],
         [10,10], [11,10], [10,11], [11,11],
         [5,20], [5,21], [6,20], [6,21]]
    labels, centroids = kmeans(X, k=3)
    for p, lab in zip(X, labels):
        print(p, "->", lab)
    print("centroids:", centroids)
