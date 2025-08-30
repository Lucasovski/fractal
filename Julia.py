import numpy as np
import matplotlib.pyplot as plt

largura = 800
altura = 800
centro_x = -0.7
centro_y = 0.27015
ampliacao = 1.0
max_iteracoes = 100
c = complex(-0.7, 0.27015)

x_largura = 4.0 / ampliacao
x_minimo = centro_x - x_largura / 2
x_maximo = centro_x + x_largura / 2
y_altura = x_largura * altura / largura
y_minimo = centro_y - y_altura / 2
y_maximo = centro_y + y_altura / 2

valores_x = np.linspace(x_minimo, x_maximo, largura)
valores_y = np.linspace(y_minimo, y_maximo, altura)
X, Y = np.meshgrid(valores_x, valores_y)
Z = X + 1j * Y
C = np.full((altura, largura), c)
matriz_iteracoes = np.zeros((altura, largura))
pontos_vivos = np.ones((altura, largura), dtype=bool)

for iteracao in range(max_iteracoes):
    Z[pontos_vivos] = Z[pontos_vivos]**2 + C[pontos_vivos]
    pontos_escaparam = (np.abs(Z) > 2) & pontos_vivos
    matriz_iteracoes[pontos_escaparam] = iteracao
    pontos_vivos[pontos_escaparam] = False

plt.imshow(matriz_iteracoes, extent=[x_minimo, x_maximo, y_minimo, y_maximo], cmap='hot')
plt.show()