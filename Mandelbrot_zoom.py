import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

class MandelbrotZoom:
    def __init__(self):
        # Configurações iniciais
        self.x_center, self.y_center = -0.725, -0.26
        self.zoom_level = 0.3
        self.max_iter = 50
        self.width, self.height = 800, 600
        self.zoom_factor = 2.0
        
        # Configurar a figura e os botões
        self.fig, self.ax = plt.subplots(figsize=(10, 8))
        plt.subplots_adjust(bottom=0.2)
        
        # Criar botões
        ax_zoom_in = plt.axes([0.7, 0.05, 0.1, 0.075])
        ax_zoom_out = plt.axes([0.81, 0.05, 0.1, 0.075])
        ax_reset = plt.axes([0.59, 0.05, 0.1, 0.075])
        
        self.btn_zoom_in = Button(ax_zoom_in, 'Zoom In')
        self.btn_zoom_out = Button(ax_zoom_out, 'Zoom Out')
        self.btn_reset = Button(ax_reset, 'Reset')
        
        # Conectar eventos
        self.btn_zoom_in.on_clicked(self.zoom_in)
        self.btn_zoom_out.on_clicked(self.zoom_out)
        self.btn_reset.on_clicked(self.reset_view)
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        
        # Gerar a visualização inicial
        self.update_plot()
        
    def mandelbrot_set(self, xmin, xmax, ymin, ymax):
        # Criar uma grade de números complexos
        x = np.linspace(xmin, xmax, self.width)
        y = np.linspace(ymin, ymax, self.height)
        c = x + y[:, None] * 1j
        
        # Inicializar arrays
        z = np.zeros_like(c)
        escape_time = np.zeros(c.shape, dtype=int)
        mask = np.ones(c.shape, dtype=bool)
        
        # Calcular o conjunto de Mandelbrot
        for i in range(self.max_iter):
            z[mask] = z[mask]**2 + c[mask]
            new_mask = (np.abs(z) < 4.0) & mask
            escape_time[new_mask ^ mask] = i
            mask = new_mask
            
            if not np.any(mask):
                break
        
        escape_time[mask] = self.max_iter
        return escape_time
    
    def update_plot(self):
        # Calcular limites atuais
        x_min = self.x_center - self.zoom_level
        x_max = self.x_center + self.zoom_level
        y_min = self.y_center - self.zoom_level * (self.height/self.width)
        y_max = self.y_center + self.zoom_level * (self.height/self.width)
        
        # Gerar o fractal
        mandelbrot = self.mandelbrot_set(x_min, x_max, y_min, y_max)
        
        # Atualizar o plot
        self.ax.clear()
        self.ax.imshow(mandelbrot, extent=(x_min, x_max, y_min, y_max), 
                      cmap='hot', origin='lower', interpolation='bilinear')
        self.ax.set_title(f'Centro: ({self.x_center:.6f}, {self.y_center:.6f}), Zoom: {self.zoom_level:.6f}')
        self.fig.canvas.draw()
    
    def on_click(self, event):
        if event.inaxes != self.ax:
            return
        
        # Definir novo centro baseado no clique
        self.x_center, self.y_center = event.xdata, event.ydata
        self.update_plot()
    
    def zoom_in(self, event):
        self.zoom_level /= self.zoom_factor
        self.update_plot()
    
    def zoom_out(self, event):
        self.zoom_level *= self.zoom_factor
        self.update_plot()
    
    def reset_view(self, event):
        self.x_center, self.y_center = -0.725, -0.26
        self.zoom_level = 0.3
        self.update_plot()

# Criar e mostrar a interface interativa
mandelbrot_zoom = MandelbrotZoom()
plt.show()