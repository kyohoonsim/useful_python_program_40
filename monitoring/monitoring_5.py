import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
from collections import deque
import numpy as np
import winsound as ws

index = count()

x = deque(maxlen=20)
y1 = deque(maxlen=20)
y2 = deque(maxlen=20)

plt.style.use('dark_background')

def beep_sound():
    freq = 2000
    dur = 200
    ws.Beep(freq, dur)

def check():
    memory_usage = psutil.virtual_memory()
    memory_used_percent = memory_usage[2]
    cpu_used_percent = psutil.cpu_percent(interval=0.5)
    return memory_used_percent, cpu_used_percent

def animate(_):
    memory, cpu = check()

    if max(memory, cpu) >= 80:
        print(beep_sound())

    x.append(next(index))
    y1.append(memory)
    y2.append(cpu)

    plt.cla()
    plt.plot(x, y1, label='memory', linewidth=0.5)
    plt.plot(x, y2, label='CPU', linewidth=0.5)
    plt.legend(loc='best')
    plt.grid(True, color='lightblue', alpha=0.3)
    plt.ylim(0, 120)
    plt.ylabel('usage %')
    plt.xticks(x)
    plt.yticks(np.arange(0, 121, 10))
    plt.fill_between(x, y1, alpha=0.2)
    plt.fill_between(x, y2, alpha=0.2)
    plt.title('Memory/CPU Monitor')

realtime_plot = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.show()
