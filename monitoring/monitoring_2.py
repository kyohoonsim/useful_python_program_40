import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count

index = count()
x, y1, y2 = [], [], []

def check():
    memory_usage = psutil.virtual_memory()
    memory_used_percent = memory_usage[2]
    cpu_used_percent = psutil.cpu_percent(interval=0.5)
    return memory_used_percent, cpu_used_percent

def animate(_):
    memory, cpu = check()

    x.append(next(index))
    y1.append(memory)
    y2.append(cpu)

    plt.cla()
    plt.plot(x, y1, label='memory')
    plt.plot(x, y2, label='CPU')
    plt.legend(loc='best')
    plt.grid(True)
    plt.ylim(0, 120)
    plt.ylabel('usage %')

realtime_plot = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.show()
