"""A 2-layer neural network from scratch -- solves XOR (the problem a single
perceptron CANNOT solve).

Architecture:
    input (2) -> hidden (4, tanh) -> output (1, sigmoid)

We hand-code:
  * the forward pass     (matrix multiply + activation)
  * the loss             (binary cross-entropy)
  * backpropagation      (chain rule, by hand)
  * gradient descent     (subtract lr * grad)

If you understand this file, you understand the core of every modern
deep-learning framework. The rest is engineering: GPUs, autograd, scale.
"""

import math
import random


def sigmoid(x):
    if x >= 0:
        z = math.exp(-x)
        return 1 / (1 + z)
    z = math.exp(x)
    return z / (1 + z)


def tanh(x):  return math.tanh(x)
def dtanh(y): return 1 - y * y                # derivative given y = tanh(x)


def make_matrix(rows, cols, scale=1.0):
    return [[random.uniform(-scale, scale) for _ in range(cols)] for _ in range(rows)]


def matvec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


def add(a, b):  return [x + y for x, y in zip(a, b)]


class NN:
    def __init__(self, n_in=2, n_hidden=4, seed=1):
        random.seed(seed)
        self.W1 = make_matrix(n_hidden, n_in)
        self.b1 = [0.0] * n_hidden
        self.W2 = make_matrix(1, n_hidden)
        self.b2 = [0.0]

    def forward(self, x):
        z1 = add(matvec(self.W1, x), self.b1)
        h  = [tanh(z) for z in z1]
        z2 = add(matvec(self.W2, h), self.b2)
        y  = sigmoid(z2[0])
        cache = (x, h, y)
        return y, cache

    def backward(self, cache, y_true):
        x, h, y = cache
        # dL/dz2 for binary cross-entropy + sigmoid simplifies to (y - y_true)
        dz2 = y - y_true
        dW2 = [[dz2 * h_j for h_j in h]]
        db2 = [dz2]
        # back into hidden layer
        dh = [self.W2[0][j] * dz2 for j in range(len(h))]
        dz1 = [dh[j] * dtanh(h[j]) for j in range(len(h))]
        dW1 = [[dz1[i] * x[k] for k in range(len(x))] for i in range(len(dz1))]
        db1 = dz1[:]
        return dW1, db1, dW2, db2

    def step(self, grads, lr):
        dW1, db1, dW2, db2 = grads
        for i in range(len(self.W1)):
            for j in range(len(self.W1[0])):
                self.W1[i][j] -= lr * dW1[i][j]
            self.b1[i] -= lr * db1[i]
        for j in range(len(self.W2[0])):
            self.W2[0][j] -= lr * dW2[0][j]
        self.b2[0] -= lr * db2[0]


def train_xor():
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]
    Y = [0, 1, 1, 0]                          # XOR truth table

    net = NN()
    lr = 0.5
    for epoch in range(8000):
        total_loss = 0.0
        for x, y in zip(X, Y):
            y_hat, cache = net.forward(x)
            eps = 1e-9
            loss = -(y * math.log(y_hat + eps) + (1 - y) * math.log(1 - y_hat + eps))
            total_loss += loss
            grads = net.backward(cache, y)
            net.step(grads, lr)
        if epoch % 1000 == 0:
            print(f"epoch {epoch:4d}  loss={total_loss:.4f}")

    print("\nPredictions after training:")
    for x, y in zip(X, Y):
        y_hat, _ = net.forward(x)
        print(f"  {x} -> {y_hat:.3f}   (target {y})")


if __name__ == "__main__":
    train_xor()
