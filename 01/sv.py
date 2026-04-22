import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

X = np.array([
    [1,2], [2,3], [3,3],
    [6,7], [7,8], [8,8]
])
y = np.array([0,0,0,1,1,1])
model = svm.SVC(kernel='linear')
print("Weights:", model.coef_)
print("Intercept:", model.intercept_)
for i in range(len(X)):

    plt.scatter(X[i][0], X[i][1])
w = model.coef_[0]
b = model.intercept_[0]
x1 = np.linspace(0, 10, 100)
x2 = -(w[0]*x1 + b) / w[1]
plt.plot(x1, x2)
plt.show()