import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('p.dat')

x = np.linspace(0, 1, data.shape[0])
y = np.linspace(0, 1, data.shape[1])
X, Y = np.meshgrid(x, y)

plt.contourf(X, Y, data, alpha=0.5, cmap=plt.cm.viridis)
plt.colorbar()
plt.contour(X, Y, data, cmap=plt.cm.viridis)
plt.show()
