import numpy as np
import matplotlib.pyplot as plt

# === Etapa 1: Definir os 8 centros (exceto o central) ===
# O quadrado grande vai de (0,0) a (1,1)
# Dividido em 3x3, cada subquadrado tem lado 1/3
# Calculamos os centros dos 8 subquadrados (ignorando o do meio)

centros = []
for linha in range(3):
    for coluna in range(3):
        if linha == 1 and coluna == 1:  # Pula o centro (buraco)
            continue
        # Posição do centro do subquadrado
        x = coluna / 3 + 1/6   # 1/6 = metade do lado (1/3) → centro
        y = linha / 3 + 1/6
        centros.append([x, y])

centros = np.array(centros)  # Converte para array NumPy

# === Etapa 2: Parâmetros do Jogo do Caos ===
num_pontos = 1000000           # Número de pontos a gerar
pontos = np.zeros((num_pontos, 2))

# Ponto inicial: escolha aleatória dentro do quadrado
pontos[0] = [np.random.random(), np.random.random()]

# === Etapa 3: Iterações do Jogo ===
for i in range(1, num_pontos):
    # Escolhe um dos 8 centros aleatoriamente
    centro_escolhido = centros[np.random.randint(0, 8)]
    
    # Move 2/3 do caminho do ponto atual até o centro escolhido
    pontos[i] = pontos[i-1] + (centro_escolhido - pontos[i-1]) * (2/3)

# === Etapa 4: Visualização ===
plt.figure(figsize=(8, 8))
plt.scatter(pontos[:, 0], pontos[:, 1], s=0.1, color='black', alpha=0.7)
plt.title("Jogo do Caos - Tapete de Sierpiński")
plt.axis('equal')      # Mantém proporção 1:1
plt.axis('off')        # Oculta eixos
plt.tight_layout()
plt.show()