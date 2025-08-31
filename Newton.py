import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da imagem
width, height = 800, 800
max_iter = 50
tolerance = 1e-6

# Limites do plano complexo
x_min, x_max = -2.0, 2.0
y_min, y_max = -2.0, 2.0

# Função f(z) = z^3 - 1
def f(z):
    return z**3 - 1

# Derivada f'(z) = 3z^2
def df(z):
    return 3 * z**2

# Método de Newton
def newton_fractal(z, max_iter=50, tol=1e-6):
    for i in range(max_iter):
        fz = f(z)
        if abs(fz) < tol:
            break
        dfz = df(z)
        if abs(dfz) < 1e-10:  # Evita divisão por zero
            return float('inf'), i
        z = z - fz / dfz
    return z, i

# Raízes exatas de z^3 - 1 = 0 (raízes cúbicas da unidade)
roots = [
    np.array([1, 0]),           # 1
    np.array([-0.5, np.sqrt(3)/2]),  # e^(2πi/3)
    np.array([-0.5, -np.sqrt(3)/2])  # e^(4πi/3)
]

def identify_root(z, roots, tol=1e-3):
    diff = np.abs(z - roots)
    for i, d in enumerate(diff):
        if np.linalg.norm(d) < tol:
            return i
    return len(roots)  # caso não identifique (cor preta)

# Criação da grade de pontos complexos
x = np.linspace(x_min, x_max, width)
y = np.linspace(y_min, y_max, height)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Matriz para armazenar a cor de cada pixel
image = np.zeros((height, width))

# Aplica o método de Newton para cada ponto
for i in range(width):
    for j in range(height):
        z = Z[j, i]
        final_z, iterations = newton_fractal(z, max_iter, tolerance)
        
        # Identifica para qual raiz convergiu
        root_index = identify_root(
            np.array([final_z.real, final_z.imag]),
            roots
        )
        image[j, i] = root_index + 0.5 * (iterations / max_iter)  # mistura raiz + iterações

# Mostra a imagem
plt.figure(figsize=(8, 8))
plt.imshow(image, extent=(x_min, x_max, y_min, y_max), cmap='hsv')  # hsv dá cores bonitas
plt.colorbar(label='Raiz + Iterações')
plt.title('Fractal de Newton para $z^3 - 1$')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.tight_layout()
plt.show()