import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def deriv(x):
    return x * (1 - x)
X = np.array([
    [1,0,1,0],
    [1,0,1,1],
    [0,1,0,1]
])
y = np.array([[1],[1],[0]])
np.random.seed(1)
W1 = np.random.rand(4,3)
b1 = np.zeros((1,3))
W2 = np.random.rand(3,1)
b2 = np.zeros((1,1))
lr = 0.1
for _ in range(5000):
    hidden = sigmoid(np.dot(X, W1) + b1)
    output = sigmoid(np.dot(hidden, W2) + b2)
    error = y - output
    d_output = error * deriv(output)
    d_hidden = np.dot(d_output, W2.T) * deriv(hidden)
    W2 += np.dot(hidden.T, d_output) * lr
    b2 += np.sum(d_output, axis=0, keepdims=True) * lr
    W1 += np.dot(X.T, d_hidden) * lr
    b1 += np.sum(d_hidden, axis=0, keepdims=True) * lr
print("Predicted Output:")
print(output)