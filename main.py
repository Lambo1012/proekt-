import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, TextBox, CheckButtons, RadioButtons
import datetime
import time

# =================================================================
# СЕРВИСНЫЙ МОДУЛЬ
# =================================================================

class LabLogger:
    def __init__(self, filename="lab_log.txt"):
        self.filename = filename
    
    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        print(log_entry)
        try:
            with open(self.filename, "a", encoding="utf-8") as f:
                f.write(log_entry + "\n")
        except Exception as e:
            print(f"Ошибка записи лога: {e}")

# =================================================================
# МАТЕМАТИЧЕСКИЙ ДВИЖОК
# =================================================================

class MathEngine:
    def __init__(self):
        self.lib = {
            'np': np, 'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
            'exp': np.exp, 'sqrt': np.sqrt, 'abs': np.abs,
            'log': np.log, 'pi': np.pi, 'where': np.where
        }

    def solve(self, formula, x_data, k_val, p_val):
        try:
            ctx = self.lib.copy()
            ctx.update({'x': x_data, 'k': k_val, 'p': p_val})
            # Безопасное вычисление формулы
            res = eval(formula, {"__builtins__": None}, ctx)
            if np.isscalar(res): 
                res = np.full_like(x_data, res)
            arr = np.array(res, dtype=float)
            arr[~np.isfinite(arr)] = np.nan
            return arr
        except Exception as e:
            print(f"Ошибка в формуле: {e}")
            return None

# =================================================================
# ОКНО ГРАФИКА (PLOT WINDOW)
# =================================================================

class PlotWindow:
    def __init__(self, engine, logger, formula, title):
        self.engine, self.logger, self.title = engine, logger, title
        self.fig, self.ax = plt.subplots(figsize=(10, 7))
        self.fig.canvas.manager.set_window_title(title)
        plt.subplots_adjust(bottom=0.35, left=0.1, right=0.75, top=0.9)
        
        self.ax.set_facecolor('#ffffff')
        self.ax.grid(True, which='major', color='#cccccc', lw=0.8)
        
        # Начальное состояние
        self.state = {
            'f': formula, 'k': 1.0, 'p': 0.0,
            'x_min': -10.0, 'x_max': 10.0,
            'color': 'blue'
        }
        self.x = np.linspace(self.state['x_min'], self.state['x_max'], 1000)
        
        y = self.engine.solve(self.state['f'], self.x, self.state['k'], self.state['p'])
        self.line, = self.ax.plot(self.x, y, color=self.state['color'], lw=2)
        
        # Инструменты анализа (точка при наведении)
        self.dot, = self.ax.plot([0], [0], 'ro', ms=6, visible=False, zorder=10)
        self.note = self.ax.annotate("", xy=(0,0), xytext=(10,10), 
                                    textcoords='offset points',
                                    bbox=dict(boxstyle='round', fc='white', alpha=0.7))
        
        self._setup_ui()
        self.fig.canvas.mpl_connect('motion_notify_event', self._hover)

    def _setup_ui(self):
        # Поле формулы
        ax_f = plt.axes([0.15, 0.22, 0.45, 0.04])
        self.tbox_f = TextBox(ax_f, 'Formula: ', initial=self.state['f'])
        self.tbox_f.on_submit(self._update_formula)

        # Слайдеры K и P
        ax_k = plt.axes([0.15, 0.14, 0.45, 0.03])
        self.sld_k = Slider(ax_k, 'Param K: ', -10.0, 10.0, valinit=1.0)
        self.sld_k.on_changed(self._refresh)

        ax_p = plt.axes([0.15, 0.08, 0.45, 0.03])
        self.sld_p = Slider(ax_p, 'Param P: ', -10.0, 10.0, valinit=0.0)
        self.sld_p.on_changed(self._refresh)

        # Выбор цвета
        ax_rad = plt.axes([0.8, 0.5, 0.15, 0.2], facecolor='#f9f9f9')
        self.radio = RadioButtons(ax_rad, ('Blue', 'Red', 'Green', 'Purple'))
        self.radio.on_clicked(self._change_color)

        # Кнопка сохранения
        ax_btn = plt.axes([0.8, 0.1, 0.15, 0.06])
        self.btn_save = Button(ax_btn, 'SAVE PNG', color='#e1f5fe')
        self.btn_save.on_clicked(self._export)

    def _update_formula(self, text):
        self.state['f'] = text
        self._refresh(None)

    def _change_color(self, label):
        self.state['color'] = label.lower()
        self.line.set_color(self.state['color'])
        self.fig.canvas.draw_idle()

    def _refresh(self, val):
        self.state['k'] = self.sld_k.val
        self.state['p'] = self.sld_p.val
        y = self.engine.solve(self.state['f'], self.x, self.state['k'], self.state['p'])
        if y is not None:
            self.line.set_data(self.x, y)
            # Автоматическое масштабирование оси Y
            valid_y = y[np.isfinite(y)]
            if len(valid_y) > 0:
                self.ax.set_ylim(min(valid_y)-0.5, max(valid_y)+0.5)
        self.fig.canvas.draw_idle()

    def _export(self, event):
        fname = f"plot_{int(time.time())}.png"
        self.fig.savefig(fname)
        self.logger.log(f"График сохранен как {fname}")

    def _hover(self, event):
        if event.inaxes == self.ax:
            x_val = event.xdata
            # Вычисляем Y для конкретной точки X под курсором
            y_arr = self.engine.solve(self.state['f'], np.array([x_val]), self.state['k'], self.state['p'])
            if y_arr is not None:
                y_val = y_arr[0]
                self.dot.set_data([x_val], [y_val])
                self.dot.set_visible(True)
                self.note.xy = (x_val, y_val)
                self.note.set_text(f"x={x_val:.2f}\ny={y_val:.2f}")
                self.note.set_visible(True)
        else:
            self.dot.set_visible(False)
            self.note.set_visible(False)
        self.fig.canvas.draw_idle()

# =================================================================
# ПАНЕЛЬ УПРАВЛЕНИЯ (MAIN MENU)
# =================================================================

class ControlPanel:
    def __init__(self):
        plt.ion()
        self.logger = LabLogger()
        self.engine = MathEngine()
        self.windows = [] # Список для хранения открытых окон
        
        self.menu_fig = plt.figure("ГЛАВНОЕ МЕНЮ", figsize=(6, 8), facecolor='#263238')
        self.ax_menu = self.menu_fig.add_subplot(111)
        self.ax_menu.axis('off')
        
        plt.text(0.5, 0.92, "Аналитический модуль", ha='center', color='white', weight='bold', size=16)
        plt.text(0.5, 0.88, "Информационные системы", ha='center', color='#b0bec5', size=10)
        
        configs = [
            ("ПАРАБОЛА", "k * x**2 + p", 0.70, '#4fc3f7'),
            ("СИНУСОИДА", "np.sin(x*k) * p", 0.58, '#4fc3f7'),
            ("ОСОБЫЙ ОПЫТ", "np.exp(x/k) + p", 0.46, '#4fc3f7'),
            ("ЗАКРЫТЬ ВСЁ", "EXIT", 0.15, '#ff5252')
        ]
        
        self.btns = []
        for txt, formula, y, color in configs:
            ax_b = plt.axes([0.15, y, 0.7, 0.07])
            btn = Button(ax_b, txt, color=color, hovercolor='#ffffff')
            btn.label.set_weight('bold')
            
            if formula == "EXIT":
                btn.on_clicked(lambda e: plt.close('all'))
            else:
                # ВАЖНО: используем замыкание для передачи параметров
                btn.on_clicked(self._make_callback(formula, txt))
                
            self.btns.append(btn)

    def _make_callback(self, f, t):
        """Создает функцию-обработчик для каждой кнопки."""
        return lambda event: self.windows.append(PlotWindow(self.engine, self.logger, f, t))

    def run(self):
        print("Приложение запущено. Нажмите кнопки в меню.")
        while plt.fignum_exists(self.menu_fig.number):
            plt.pause(0.1)

if __name__ == "__main__":
    # Теперь здесь нет пустых заглушек, вызываются реальные классы
    app = ControlPanel()
    app.run()