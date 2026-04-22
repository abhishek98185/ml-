import numpy as np
import matplotlib.pyplot as plt
from numpy import loadtxt, where, zeros, log, ones, array
from pylab import scatter, show, legend, xlabel, ylabel, plot
from scipy.optimize import fmin_bfgs
import math

def sigmoid(X):
    g = 1 / (1 + np.exp(-X))
    return g
def costFunction(theta, X, y):
    m = y.size
    theta = theta.reshape((X.shape[1], 1))
    
    h = sigmoid(X.dot(theta))
    
    J = (-1/m) * (y.T.dot(log(h)) + (1 - y).T.dot(log(1 - h)))
    return J[0, 0]
def gradFunction(theta, X, y):
    m = y.size
    theta = theta.reshape((X.shape[1], 1))
    
    h = sigmoid(X.dot(theta))
    delta = h - y
    
    grad = (1/m) * (X.T.dot(delta))
    return grad.flatten()
data = loadtxt('C:/Users/abhis/Documents/DTU ML_LAB/experiment 6/ex2data1.txt', delimiter=',')
X = data[:, 0:2]
y = data[:, 2]

y = y.reshape((y.size, 1))

pos = where(y == 1)
neg = where(y == 0)

scatter(X[pos, 0], X[pos, 1], marker='o', c='b')
scatter(X[neg, 0], X[neg, 1], marker='x', c='r')
xlabel('X')
ylabel('Y')
legend(['Admitted', 'Not Admitted'])
show()
m, n = X.shape
X_new = ones((m, n + 1))
X_new[:, 1:] = X
def learning_parameters(X, y):
    initial_theta = zeros(X.shape[1])
    
    theta = fmin_bfgs(
        costFunction,
        initial_theta,
        fprime=gradFunction,
        args=(X, y),
        maxiter=400,
        disp=True
    )
    return theta

theta = learning_parameters(X_new, y)
print("Optimized Theta:", theta)
plot_x = array([min(X[:, 0]) - 2, max(X[:, 0]) + 2])
plot_y = (-1/theta[2]) * (theta[1] * plot_x + theta[0])

plot(plot_x, plot_y)
scatter(X[pos, 0], X[pos, 1], marker='o', c='b')
scatter(X[neg, 0], X[neg, 1], marker='x', c='r')
legend(['Decision Boundary', 'Admitted', 'Not Admitted'])
show()
prob = sigmoid(array([1, 45, 85]).dot(theta))
print("Probability:", prob)
def predict(theta, X):
    h = sigmoid(X.dot(theta))
    p = zeros((h.shape[0], 1))
    
    for i in range(h.shape[0]):
        if h[i] >= 0.5:
            p[i] = 1
        else:
            p[i] = 0
    return p
p = predict(theta, X_new)
accuracy = (p == y).mean() * 100
print("Train Accuracy:", accuracy, "%")
