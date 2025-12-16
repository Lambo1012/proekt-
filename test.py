import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def plot_sympy_function(expr_str, x_range=(-10, 10)):
    """
    Построение графика с использованием SymPy для аналитических вычислений
    """
    # Определяем символьную переменную
    x = sp.symbols('x')
    
    try:
        # Парсим выражение
        expr = sp.sympify(expr_str)
        
        # Преобразуем в функцию для вычислений
        f = sp.lambdify(x, expr, 'numpy')
        
        # Создаем числовой диапазон
        x_vals = np.linspace(x_range[0], x_range[1], 1000)
        y_vals = f(x_vals)
        
        # Создаем график
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # График функции
        ax1.plot(x_vals, y_vals, 'b-', linewidth=2)
        ax1.set_title(f'График функции: {sp.pretty(expr)}', fontsize=14)
        ax1.set_xlabel('x')
        ax1.set_ylabel('f(x)')
        ax1.grid(True, alpha=0.3)
        ax1.axhline(y=0, color='k', linewidth=0.5)
        ax1.axvline(x=0, color='k', linewidth=0.5)
        
        # Находим производную
        derivative = sp.diff(expr, x)
        f_prime = sp.lambdify(x, derivative, 'numpy')
        y_prime_vals = f_prime(x_vals)
        
        # График производной
        ax2.plot(x_vals, y_prime_vals, 'r-', linewidth=2)
        ax2.set_title(f'Производная: {sp.pretty(derivative)}', fontsize=14)
        ax2.set_xlabel('x')
        ax2.set_ylabel("f'(x)")
        ax2.grid(True, alpha=0.3)
        ax2.axhline(y=0, color='k', linewidth=0.5)
        ax2.axvline(x=0, color='k', linewidth=0.5)
        
        plt.tight_layout()
        plt.show()
        
        # Выводим дополнительную информацию
        print("Анализ функции:")
        print(f"Функция: {expr}")
        print(f"Производная: {derivative}")
        
        # Находим корни (если возможно)
        try:
            roots = sp.solve(expr, x)
            if roots:
                print(f"Корни: {roots}")
        except:
            pass
        
    except Exception as e:
        print(f"Ошибка: {e}")

# Примеры использования
if __name__ == "__main__":
    # Пример 1
    plot_sympy_function("x**2 - 4")
    
    # Пример 2
    # plot_sympy_function("sin(x)")
    
    # Пример 3
    # plot_sympy_function("exp(-x/5) * sin(x)")