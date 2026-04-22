import numpy as np
import matplotlib.pyplot as plt
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
X = np.array([
    2, 3, 2, 3, 2.5,
    -2,-1, -3,-2, -2
])

y = np.array([
    1,1,1,1,1,
    0,0,0,0,0
])
w = 0
b = 0
lr = 0.1
epochs = 1000
n = len(X)
for _ in range(epochs):
    z = w * X + b
    y_pred = sigmoid(z)
    dw = (1/n) * np.sum((y_pred - y) * X)
    db = (1/n) * np.sum(y_pred - y)
    w = w - lr * dw
    b = b - lr * db
print(w, b)
probs = sigmoid(w * X + b)
predictions = []
for i in range(n):
    if probs[i] >= 0.5:
        predictions.append(1)
    else:
        predictions.append(0)

print(probs)
print(predictions)
z = w * X + b
probs = 1 / (1 + np.exp(-z))

