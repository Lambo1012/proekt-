import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation
import matplotlib

matplotlib.use('TkAgg')

# Создаем граф
G = nx.Graph()

# Функция сердца
def heart_function(t):
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return x, y

# Создаем узлы на контуре сердца
n_nodes = 40
for i in range(n_nodes):
    t = 2 * np.pi * i / n_nodes
    x, y = heart_function(t)
    G.add_node(i, pos=(x, y))
    
    # Соединяем узлы
    if i > 0:
        G.add_edge(i-1, i)
G.add_edge(n_nodes-1, 0)  # Замыкаем контур

# Добавляем несколько внутренних узлов
for i in range(n_nodes, n_nodes + 20):
    t = np.random.uniform(0, 2*np.pi)
    scale = np.random.uniform(0.3, 0.8)
    x, y = heart_function(t)
    G.add_node(i, pos=(x*scale, y*scale))
    
    # Соединяем с соседями
    for j in range(max(0, i-5), i):
        if np.random.random() > 0.5:
            G.add_edge(i, j)

# Настройка визуализации
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-20, 20)
ax.set_ylim(-18, 18)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('black')
fig.patch.set_facecolor('black')

pos = nx.get_node_attributes(G, 'pos')

def animate(frame):
    ax.clear()
    ax.set_xlim(-20, 20)
    ax.set_ylim(-18, 18)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_facecolor('black')
    
    # Пульсация
    scale = 1 + 0.1 * np.sin(frame * 0.3)
    
    # Масштабируем позиции
    scaled_pos = {node: (p[0]*scale, p[1]*scale) for node, p in pos.items()}
    
    # Рисуем граф
    nx.draw_networkx_edges(G, scaled_pos, 
                          edge_color='red', 
                          alpha=0.3,
                          width=1,
                          ax=ax)
    
    # Рисуем узлы
    node_colors = []
    node_sizes = []
    for node in G.nodes():
        if node < n_nodes:
            # Узлы контура
            node_colors.append('red')
            node_sizes.append(50)
        else:
            # Внутренние узлы
            if node % 3 == 0:
                node_colors.append('white')
            else:
                node_colors.append('red')
            node_sizes.append(30)
    
    nx.draw_networkx_nodes(G, scaled_pos,
                          node_color=node_colors,
                          node_size=node_sizes,
                          alpha=0.8,
                          ax=ax)
    
    # Текст
    text_color = 'white' if frame % 30 < 15 else 'red'
    ax.text(0, -14, 'LOVE', color=text_color, 
           fontsize=24, ha='center', fontweight='bold')
    
    return ax,

# Запуск анимации
anim = FuncAnimation(fig, animate, frames=300, interval=50, blit=False)
plt.show()