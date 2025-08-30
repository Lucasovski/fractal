import numpy as np
import matplotlib.pyplot as plt

largura, altura = 800, 800
max_iter = 100
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5

eixo_x = np.linspace(x_min, x_max, largura)
eixo_y = np.linspace(y_min, y_max, altura)
c = eixo_x[:, np.newaxis] + 1j * eixo_y[np.newaxis, :]
z = np.zeros(c.shape, dtype=np.complex128)
nao_divergiu = np.ones(c.shape, dtype=bool)
iteracao = np.zeros(c.shape, dtype=int)

for i in range(max_iter):
    z[nao_divergiu] = z[nao_divergiu]**2 + c[nao_divergiu]
    divergindo = (np.abs(z) > 2) & nao_divergiu
    nao_divergiu[divergindo] = False
    iteracao[divergindo] = i

imagem = iteracao.astype(float)
misiurewicz = np.zeros((altura, largura), dtype=bool)

def eh_misiurewicz(c_valor, max_iter=100, tol=1e-5):
    z = 0
    for _ in range(max_iter):
        z = z*z + c_valor
        if abs(z) > 2:
            return False
    tartaruga = c_valor
    coelho = c_valor*c_valor + c_valor
    while abs(tartaruga - coelho) > tol:
        tartaruga = tartaruga*tartaruga + c_valor
        coelho = (coelho*coelho + c_valor)**2 + c_valor
        if abs(tartaruga) > 2 or abs(coelho) > 2:
            return False
    mi = 0
    tartaruga = 0
    while abs(tartaruga - coelho) > tol:
        tartaruga = tartaruga*tartaruga + c_valor
        coelho = coelho*coelho + c_valor
        mi += 1
    return mi > 0

for i in range(altura):
    for j in range(largura):
        if nao_divergiu[j, i]:
            if eh_misiurewicz(c[j, i], max_iter=100):
                misiurewicz[i, j] = True

indices_i, indices_j = np.where(misiurewicz)
pontos_misiurewicz = [c[j, i] for i, j in zip(indices_i, indices_j)]
print(pontos_misiurewicz)

plt.figure(figsize=(10, 10))
plt.imshow(imagem.T, extent=[x_min, x_max, y_min, y_max], cmap='hot', interpolation='bilinear')
plt.scatter(np.where(misiurewicz)[1] * (x_max - x_min) / largura + x_min,
            np.where(misiurewicz)[0] * (y_max - y_min) / altura + y_min,
            color='red', s=0.1)
plt.title('Conjunto de Mandelbrot com Pontos de Misiurewicz')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.show()