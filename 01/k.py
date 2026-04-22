import numpy as np
import matplotlib.pyplot as plt
X = np.array([[1,2],
              [2,3],
              [3,4],
              [6,7],
              [7,8]])
y = np.array([0, 0, 0, 1, 1])
k = 3
def distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))
x_new = np.array([5,6])
distances = []
for i in range(len(X)):
    d = distance(X[i], x_new)
    distances.append((d, y[i]))
distances.sort()
neighbors = distances[:k]
count0 = 0
count1 = 0
for d, label in neighbors:
    if label == 0:
        count0 += 1
    else:
        count1 += 1
if count1 > count0:
    print(1)
else:
    print(0)