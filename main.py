!pip install imageio

import matplotlib.pyplot as plt
import random
import imageio
import time
import numpy as np

from matplotlib.animation import FuncAnimation


def generar_puntos_cuadrados(x, y, num_puntos):
    puntos = []
    for _ in range(num_puntos):
        punto = (random.uniform(0, x), random.uniform(0, y))
        puntos.append(punto)
    return puntos

def generar_triangulos(num_triangulos):
    triangulos = []
    for _ in range(num_triangulos):
        x = float(200)  # Definir los valores de entrada
        y = float(200)
        num_puntos = 3
        puntos = generar_puntos_cuadrados(x, y, num_puntos)
        triangulos.append(puntos)
    return triangulos

def update(frame):
    plt.clf()  # Limpiar la figura
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim(-margen, x + margen)
    plt.ylim(-margen, y + margen)
    plt.plot([0, x, x, 0, 0], [0, 0, y, y, 0], color='blue')
    puntos_x = [p[0] for p in triangulos[frame]]
    puntos_y = [p[1] for p in triangulos[frame]]
    plt.scatter(puntos_x, puntos_y, color='red')
    plt.plot([triangulos[frame][0][0], triangulos[frame][1][0], triangulos[frame][2][0], triangulos[frame][0][0]], 
             [triangulos[frame][0][1], triangulos[frame][1][1], triangulos[frame][2][1], triangulos[frame][0][1]], 
             color='green')
    plt.fill([triangulos[frame][0][0], triangulos[frame][1][0], triangulos[frame][2][0], triangulos[frame][0][0]], 
             [triangulos[frame][0][1], triangulos[frame][1][1], triangulos[frame][2][1], triangulos[frame][0][1]], 
             color='green', alpha=0.3)

# Configuración inicial
x = float(200)
y = float(200)
margen = max(x, y) * 0.1  # 10% de margen alrededor del área cuadrada
num_triangulos = 10

triangulos = generar_triangulos(num_triangulos)

# Configuración de la animación
fig = plt.figure(figsize=(8, 8))
anim = FuncAnimation(fig, update, frames=num_triangulos, repeat=False)

# Guardar la animación como un archivo GIF
anim.save('triangulos.gif', writer='pillow', fps=3)
