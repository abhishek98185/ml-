import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

x = [10, 12, 13, 15, 16, 17, 19, 20]
y = [15, 18, 21, 12, 34, 21, 23, 27]

plt.scatter(x, y)
plt.title("Original Data Points")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

points = [(a, b) for a, b in zip(x, y)]

wcss = []
for k in range(1, len(points) + 1):   
    model = KMeans(n_clusters=k, n_init=10)
    model.fit(points)
    wcss.append(model.inertia_)
plt.figure()
plt.plot(range(1, len(points) + 1), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS (Inertia)")
plt.grid(True)
plt.show()
km = KMeans(n_clusters=2, n_init=10)
km.fit(points)
plt.figure()
plt.scatter(x, y, c=km.predict(points), cmap='viridis')
centers = km.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='x', s=100)

plt.title("K-Means Clustering Result")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()