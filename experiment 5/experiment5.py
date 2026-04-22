import numpy as np
import matplotlib.pyplot as plt
mydata = np.genfromtxt(r"C:/Users/abhis/Documents/DTU ML_LAB/experiment 5\Linear_regression_data.csv", delimiter=',')


X = mydata[:, 0].reshape(-1, 1)
y = mydata[:, 1].reshape(-1, 1)

ones = np.ones((X.shape[0], 1))
X = np.concatenate((ones, X), axis=1)


plt.scatter(mydata[:, 0], y)
plt.xlabel("X")
plt.ylabel("y")
plt.title("Training Data")
plt.show()


alpha = 0.0001
iters = 1000
theta = np.array([[1.0, 1.0]])


def computeCost(X, y, theta):
    predictions = X.dot(theta.T)
    errors = predictions - y
    cost = np.sum(errors ** 2) / (2 * len(X))
    return cost

print("Initial Cost:", computeCost(X, y, theta))

# Gradient Descent
def gradientDescent(X, y, theta, alpha, iters):
    m = len(X)
    cost_history = []

    for _ in range(iters):
        predictions = X.dot(theta.T)
        errors = predictions - y
        theta = theta - (alpha / m) * np.sum(errors * X, axis=0)
        cost_history.append(computeCost(X, y, theta))

    return theta, cost_history

# Run gradient descent
theta_final, cost_history = gradientDescent(X, y, theta, alpha, iters)

print("Final Theta:", theta_final)
print("Final Cost:", cost_history[-1])

# Plot regression line
plt.scatter(mydata[:, 0], y, label="Data")
x_vals = np.linspace(mydata[:, 0].min(), mydata[:, 0].max(), 100)
y_vals = theta_final[0][0] + theta_final[0][1] * x_vals
plt.plot(x_vals, y_vals, 'r--', label="Regression Line")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()
