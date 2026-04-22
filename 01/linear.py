import numpy as np
import matplotlib.pyplot as plt
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])
m = 0
b = 0
lr = 0.01
epochs = 1000
n = len(X)
for _ in range(epochs):
    y_pred = m * X + b
    dm = (-2/n) * np.sum(X * (y - y_pred))
    db = (-2/n) * np.sum(y - y_pred)
    m = m - lr * dm
    b = b - lr * db
print(m, b)
print(m * X + b)
plt.scatter(X, y)
plt.plot(X, m * X + b)
plt.show()