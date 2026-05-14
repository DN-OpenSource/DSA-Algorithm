"""The perceptron -- the first 'neuron' ever trained (Rosenblatt, 1958).

A perceptron computes  y = sign(w . x + b).
Training rule: for every misclassified point, push w toward the right answer:
    w <- w + lr * y_true * x
    b <- b + lr * y_true
Works for linearly separable data.
"""


def sign(x):
    return 1 if x >= 0 else -1


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def train(X, y, lr=1.0, epochs=20):
    w = [0.0] * len(X[0])
    b = 0.0
    for epoch in range(epochs):
        errors = 0
        for xi, yi in zip(X, y):
            pred = sign(dot(w, xi) + b)
            if pred != yi:
                errors += 1
                for j in range(len(w)):
                    w[j] += lr * yi * xi[j]
                b += lr * yi
        if errors == 0:
            print(f"converged at epoch {epoch}")
            break
    return w, b


def predict(w, b, x):
    return sign(dot(w, x) + b)


if __name__ == "__main__":
    # Linearly separable: positive y when x1+x2 > 1
    X = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2], [3, 1], [0.5, 0.4]]
    y = [-1, -1, -1, 1, 1, 1, -1]
    w, b = train(X, y)
    print("w =", w, " b =", b)
    for xi, yi in zip(X, y):
        print(f"{xi} -> pred={predict(w, b, xi):+d} true={yi:+d}")
