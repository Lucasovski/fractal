import numpy as np
import matplotlib.pyplot as plt

# Vértices do triângulo
vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])

# Parâmetros
num_points = 10000
points = np.zeros((num_points, 2))

# Ponto inicial
points[0] = [0.1, 0.1]

# Iterações
for i in range(1, num_points):
    vertex = vertices[np.random.randint(0, 3)]  # escolhe um vértice aleatório
    points[i] = (points[i-1] + vertex) / 2  # ponto médio

# Plotar
plt.figure(figsize=(8, 8))
plt.scatter(points[:, 0], points[:, 1], s=0.5, color='black')
plt.title("Chaos Game - Triângulo de Sierpiński")
plt.axis('equal')
plt.axis('off')
plt.show()