import numpy as np
from random import uniform
import matplotlib.pyplot as plt
from math import inf

N = 1000


# THIS CODE CAN BE IMPROVED: 
# BY UTILIZING NUMPY MORE, 
# BY ADDING CHECK FOR IF THE CENTROIDS ARE NOT CHANGING SIGNIFICANTLY
# BY ADDING PARALEL COMPUTATION 

# O(sample * iter * N * n_clusters)


def get_distance(a, b):
    if len(a) != len(b):
        raise ValueError('Incorrect input!')
    return sum([(a[i] - b[i]) ** 2 for i in range(len(a))]) ** 0.5


class Centroid:
    def __init__(self, cords, assigned_data) -> None:
        self.cords = cords
        self.assigned_data = assigned_data

    def get_inertia(self):
        return sum([get_distance(self.cords, data_item) ** 2 for data_item in self.assigned_data])


def k_means(data, n_clusters, iter, sample=10):
    result = []
    result_inertia = -1
    for s in range(sample):
        data_min, data_max = (np.amin(data, axis=0), np.amax(data, axis=0))

        centroids = []
        for _ in range(n_clusters):
            centroids.append(Centroid([uniform(data_min[i], data_max[i]) for i in range(data.shape[1])], []))

        for _ in range(iter):
            for data_item in data:
                distance_list = []
                for c in centroids:
                    distance_list.append(get_distance(data_item, c.cords))
                centroids[distance_list.index(min(distance_list))].assigned_data.append(data_item)
            for c in centroids:
                c.cords = np.mean(c.assigned_data, axis=0)

        inertia = sum([centroid.get_inertia() for centroid in centroids])
        if inertia < result_inertia or result_inertia == -1:
            result = centroids
            result_inertia = inertia
    
    return result
    

data = np.random.randint(0, 101, size=(1000, 2))
centroids = k_means(data, 4, 10, 100)

for i, c in enumerate(centroids):
    cluster_data = np.array(c.assigned_data)
    plt.scatter(cluster_data[:, 0], cluster_data[:, 1,])

for c in centroids:
    plt.scatter(c.cords[0], c.cords[1], marker='x', s=100, color='black')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('K-Means Clustering')
plt.show()
