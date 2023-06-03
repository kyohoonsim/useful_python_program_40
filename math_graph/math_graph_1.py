import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)
y = 2*x - 4

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
