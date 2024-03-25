import numpy as np
from random import uniform
import matplotlib.pyplot as plt
from math import inf


# THIS ALGORITHM IMPLEMENTATION IS INEFITIENT AND IS BOTH COMPUTATIONALY AND MEMORY EXPENSIVE


def dbscan(data, eps, min_points):
    distances = np.sqrt(np.sum((data[:, np.newaxis] - data) ** 2, axis=-1))
    filtered_distances =np.argwhere(eps < distances)
    init_core_points = []
    init_other_points = []
    for i, val in enumerate(data):
        if len(filtered_distances[i]) >= min_points:
            init_core_points.append(tuple([i, tuple(val)]))
            continue
        init_other_points.append(tuple([i, tuple(val)]))
    
    clusters = []
    adj_clusters = []
    for val in init_core_points:
        next_cluster = len(clusters)
        found_cluster = next_cluster
        for cluster, points in enumerate(clusters):
            if val[1] in points:
                found_cluster = cluster
                clusters[cluster].append(val[1])
        if found_cluster == next_cluster:
            clusters.append([val[1]])
            adj_clusters.append([])
        for p in data[filtered_distances[val[0]]]:
            if p in init_core_points:
                clusters[found_cluster].append(val[1])
                del init_core_points[init_core_points.index(val[1])]
            elif p in init_other_points:
                adj_clusters[found_cluster].append(val[1])
                del init_other_points[init_other_points.index(val[1])]
    
    for cluster, points in enumerate(adj_clusters):
        clusters[cluster].append(points)
    
    for cluster, points in enumerate(clusters):
        clusters[cluster] = [list(point) for point in points]
        print(clusters[cluster])
    
    return clusters




data = np.random.randint(0, 101, size=(1000, 2))
centroids = dbscan(data, 50, 2)

plt.scatter(centroids[:, 0], centroids[:, 1], label='Cluster Data')

for c in centroids:
    plt.scatter(c.cords[0], c.cords[1], marker='x', s=100, color='black')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('DBSCAN Clustering')
plt.show()
