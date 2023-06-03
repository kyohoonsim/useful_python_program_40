import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)
y = x**2 + 2*x - 3

fig, ax = plt.subplots()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
ax.plot(x, y)
plt.ylim(-5, 5)
plt.xlim(-5, 5)
plt.gca().set_aspect('equal', adjustable='box')
plt.annotate(r'$y = x^2 - 2x + 3$', xy=(1, 3), fontsize=12)
plt.annotate('x', xy=(5, -0.5), fontsize=12)
plt.annotate('y', xy=(-0.5, 5), fontsize=12)
plt.show()  