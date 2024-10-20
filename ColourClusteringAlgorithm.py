import numpy as np

def initialize_centers(data, k):
    # Випадковим чином ініціалізуємо кластерні центри
    indices = np.random.choice(len(data), k, replace=False)
    centers = [data[i] for i in indices]
    return np.array(centers)

def assign_clusters(data, centers):
    # Призначаємо кожну точку до найближчого кластеру
    clusters = []
    for point in data:
        distances = [np.linalg.norm(point - center) for center in centers]
        cluster = np.argmin(distances)
        clusters.append(cluster)
    return np.array(clusters)

def update_centers(data, clusters, k):
    # Оновлюємо центри кластерів
    centers = []
    for i in range(k):
        cluster_points = data[clusters == i]
        if len(cluster_points) > 0:
            center = np.mean(cluster_points, axis=0)
        else:
            center = np.random.choice(data, 1)
        centers.append(center)
    return np.array(centers)

def kmeans(data, k, max_iter=100):
    centers = initialize_centers(data, k)
    for _ in range(max_iter):
        clusters = assign_clusters(data, centers)
        new_centers = update_centers(data, clusters, k)
        if np.array_equal(centers, new_centers):
            break
        centers = new_centers
    return centers

# Приклад використання
colors = np.array([(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)])
k = 2  # Бажана кількість кластерів
new_centers = kmeans(colors, k)
print(new_centers)