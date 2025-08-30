import random
import cmath
import matplotlib.pyplot as plt

def calcular_pre_imagem(ponto, c_valor):
    diferenca = ponto - c_valor
    raiz = cmath.sqrt(diferenca)
    return [raiz, -raiz]

def iteracao_reversa(c_valor, total_iteracoes=10000, descartar=100):
    pontos = []
    ponto_atual = 0
    
    for _ in range(total_iteracoes):
        pre_imagens = calcular_pre_imagem(ponto_atual, c_valor)
        ponto_atual = random.choice(pre_imagens)
        pontos.append(ponto_atual)
    
    pontos_relevantes = []
    for i in range(len(pontos) - 1, descartar - 1, -1):
        pontos_relevantes.append(pontos[i])
    
    return pontos_relevantes

def plotar_conjunto_julia(c_valor, total_iteracoes=10000, descartar=100):
    pontos = iteracao_reversa(c_valor, total_iteracoes, descartar)
    
    partes_reais = [ponto.real for ponto in pontos]
    partes_imaginarias = [ponto.imag for ponto in pontos]
    
    plt.figure(figsize=(8, 8))
    plt.scatter(partes_reais, partes_imaginarias, s=0.1, color='black')
    plt.title(f'Conjunto de Julia para c = {c_valor}')
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginária')
    plt.axis('equal')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

c = -0.8 + 0.156j
plotar_conjunto_julia(c)