import numpy as np
import matplotlib.pyplot as plt

# Функция которая рисует графики
def plot_function(func, x_range=(-10, 10), num_points=1000, title="График функции"):
    # Тут мы делаем много точек по иксу от минимума до максимума
    x = np.linspace(x_range[0], x_range[1], num_points)
    
    # Считаем игрики. Если чет пойдет не так - напишем ошибку
    try:
        y = func(x)
    except:
        print("Ошибка! Функция неправильно работает")
        return
    
    # Рисуем
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='f(x)')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)  # сетка чтобы красиво было
    
    # Рисуем оси координат
    plt.axhline(y=0, color='k')  # горизонтальная линия
    plt.axvline(x=0, color='k')  # вертикальная линия
    
    plt.legend()
    plt.show()

# Тут проверяем как работает
if __name__ == "__main__":
    # Квадратичная функция
    plot_function(lambda x: x**2, x_range=(-3, 3), title="парабола")
    
    # Синус
    plot_function(lambda x: np.sin(x), x_range=(-6, 6), title="синус")
    
    # Модуль икса
    plot_function(lambda x: abs(x), x_range=(-4, 4), title="модуль")