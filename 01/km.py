import numpy as np
X = np.array([
    [1, 2], [2, 3], [3, 4],
    [8, 7], [9, 8], [10, 9]
])
k = 2
centroids = X[:k]
iterations = 10
for _ in range(iterations):
    clusters = [[] for _ in range(k)]
    for point in X:
        distances = []
        for c in centroids:
            d = np.sqrt(np.sum((point - c) ** 2))
            distances.append(d)
        cluster_index = distances.index(min(distances))
        clusters[cluster_index].append(point)
    new_centroids = []
    for cluster in clusters:
        if len(cluster) == 0:
            new_centroids.append([0, 0])
        else:
            new_centroids.append(np.mean(cluster, axis=0))
    centroids = np.array(new_centroids)
print("Final Centroids:")
for c in centroids:
    print(c)