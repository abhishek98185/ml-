import numpy as np
X = np.array([
    [1, 0, 1, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 1]
])
y = np.array([
    [1],
    [1],
    [0]
])

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)
epochs = 5000
learning_rate = 0.1
input_neurons = X.shape[1]
hidden_neurons = 3
output_neurons = 1
W_hidden = np.random.uniform(size=(input_neurons, hidden_neurons))
B_hidden = np.random.uniform(size=(1, hidden_neurons))

W_output = np.random.uniform(size=(hidden_neurons, output_neurons))
B_output = np.random.uniform(size=(1, output_neurons))

for epoch in range(epochs):
    hidden_input = np.dot(X, W_hidden) + B_hidden
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, W_output) + B_output
    predicted_output = sigmoid(final_input)

    error = y - predicted_output

    d_output = error * sigmoid_derivative(predicted_output)
    hidden_error = np.dot(d_output, W_output.T)
    d_hidden = hidden_error * sigmoid_derivative(hidden_output)

    W_output += np.dot(hidden_output.T, d_output) * learning_rate
    B_output += np.sum(d_output, axis=0, keepdims=True) * learning_rate

    W_hidden += np.dot(X.T, d_hidden) * learning_rate
    B_hidden += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate

print("Predicted Values:\n", predicted_output)