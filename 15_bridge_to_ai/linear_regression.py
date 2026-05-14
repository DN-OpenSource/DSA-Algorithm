"""Linear regression by gradient descent.

We have points (x_i, y_i) and we want to find w, b such that
    y_hat = w*x + b
fits them best (minimises mean squared error).

Gradient descent:
    repeat:
        compute gradient dL/dw, dL/db
        w -= lr * dL/dw
        b -= lr * dL/db
That tiny loop is the heart of *all* modern deep learning.
"""

import random


def fit(xs, ys, lr=0.01, epochs=1000):
    w, b = 0.0, 0.0
    n = len(xs)
    for epoch in range(epochs):
        dw, db, loss = 0.0, 0.0, 0.0
        for x, y in zip(xs, ys):
            y_hat = w * x + b
            error = y_hat - y
            loss += error * error
            dw += 2 * error * x / n
            db += 2 * error / n
        loss /= n
        w -= lr * dw
        b -= lr * db
        if epoch % 100 == 0:
            print(f"epoch {epoch:4d}  loss={loss:.4f}  w={w:.4f}  b={b:.4f}")
    return w, b


if __name__ == "__main__":
    random.seed(0)
    true_w, true_b = 2.0, -1.0
    xs = [i / 10 for i in range(50)]
    ys = [true_w * x + true_b + random.gauss(0, 0.1) for x in xs]
    w, b = fit(xs, ys)
    print(f"\nlearned y = {w:.3f} x + {b:.3f}   (true {true_w}x + {true_b})")
