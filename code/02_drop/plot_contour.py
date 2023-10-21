import numpy as np
import matplotlib.pyplot as plt

data = np.zeros([3,34,34])
data[0] = np.loadtxt('rho001.dat')
data[1] = np.loadtxt('rho010.dat')
data[2] = np.loadtxt('rho050.dat')

x = np.linspace(0, 1, 34)
y = np.linspace(0, 1, 34)
X, Y = np.meshgrid(x, y)

for i in range(3):
  data[i] = np.rot90(data[i],3)
  plt.contourf(X, Y, data[i], alpha=0.5, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.contour(X, Y, data[i], cmap=plt.cm.viridis)
  plt.show()