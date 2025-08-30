import numpy as np
import matplotlib.pyplot as plt

largura = 800
altura = 800
max_iterações = 100
centro_real = -0.5
centro_imag = 0.0
zoom = 1.0

x_min = centro_real - 1.5 / zoom
x_max = centro_real + 1.5 / zoom
y_min = centro_imag - 1.5 / zoom
y_max = centro_imag + 1.5 / zoom

eixo_x = np.linspace(x_min, x_max, largura)
eixo_y = np.linspace(y_min, y_max, altura)

c = eixo_x[np.newaxis, :] + 1j * eixo_y[:, np.newaxis]

z = np.zeros((altura, largura), dtype=complex)
iterações = np.full((altura, largura), max_iterações, dtype=int)
mascara = np.ones((altura, largura), dtype=bool)

for i in range(max_iterações):
    z[mascara] = z[mascara]**2 + c[mascara]
    escapou = np.abs(z) > 2
    iterações[escapou & mascara] = i
    mascara = mascara & ~escapou

imagem = max_iterações - iterações

plt.imshow(imagem, cmap='hot', extent=[x_min, x_max, y_min, y_max], origin='lower')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title('Conjunto de Mandelbrot')
plt.show()