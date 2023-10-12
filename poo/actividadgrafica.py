import numpy as np
import matplotlib.pyplot as plt

class Graficador:
    def __init__(self, xmin=-5, xmax=5, ymin=-1.5, ymax=1.5, num=1000):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.num = num
        
    def graficar(self):
        x = np.linspace(self.xmin, self.xmax, self.num)
        y = np.exp(-np.abs(x)) * np.cos(2 * np.pi * x)
        
        plt.plot(x, y)
        plt.axis([self.xmin, self.xmax, self.ymin, self.ymax])
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Gráfica de f(x) = e^(-|x|) * cos(2*pi*x)")
        plt.grid(True)
        plt.show()
