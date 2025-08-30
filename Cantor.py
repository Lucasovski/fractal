import matplotlib.pyplot as plt
from fractions import Fraction

def format_fraction(f):
    """Formata um Fraction como string em forma de fração reduzida"""
    if f == 0:
        return "0"
    num = f.numerator
    den = f.denominator
    if den == 1:
        return str(num)
    return f"{num}/{den}"

def plot_cantor(n):
    """
    Plota o conjunto de Cantor até n iterações com frações nas extremidades.
    
    Args:
        n: Número de iterações (0 = intervalo original)
    """
    # Gerar todos os intervalos para cada iteração
    all_intervals = []
    current = [(Fraction(0), Fraction(1))]
    all_intervals.append(current)
    
    for _ in range(n):
        new_current = []
        for (a, b) in current:
            length = b - a
            third = length / 3
            new_current.append((a, a + third))
            new_current.append((b - third, b))
        current = new_current
        all_intervals.append(current)
    
    # Configurar o gráfico
    plt.figure(figsize=(12, 6), dpi=120)
    plt.xlim(-0.02, 1.02)
    plt.ylim(-0.05, 1.05)
    plt.xlabel('x', fontsize=12)
    plt.title(f'Conjunto Ternário de Cantor (n = {n})', fontsize=14, pad=20)
    plt.grid(alpha=0.2)
    
    # Plotar cada iteração
    for i, intervals in enumerate(all_intervals):
        y = 1 - i / (n + 1)  # Posição vertical da iteração
        
        for (a, b) in intervals:
            # Plotar segmento
            plt.plot([float(a), float(b)], [y, y], 'b-', linewidth=1.5)
            
            # Adicionar rótulos nas extremidades
            for x in [a, b]:
                label = format_fraction(x)
                plt.text(
                    float(x), 
                    y - 0.015, 
                    label,
                    ha='center',
                    va='top',
                    fontsize=7 if n <= 3 else 5,
                    bbox=dict(facecolor='white', 
                              edgecolor='gray', 
                              alpha=0.7, 
                              boxstyle='round,pad=0.2')
                )
    
    # Ajustar layout e exibir
    plt.tight_layout()
    plt.show()

# Exemplo de uso (altere o valor de n conforme necessário)
if __name__ == "__main__":
    n_iter = 3  # Número de iterações (recomendado: 0-5 para boa visualização)
    plot_cantor(n_iter)