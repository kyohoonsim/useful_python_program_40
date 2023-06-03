import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)
y = 2*x - 4

fig, ax = plt.subplots()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
ax.plot(x, y)
plt.show()  