import numpy as np
import matplotlib.pyplot as plt

data = np.zeros([3,34,34])
data[0] = np.loadtxt('rho001.dat')
data[1] = np.loadtxt('rho010.dat')
data[2] = np.loadtxt('rho050.dat')

for i in range(3):
  data[i] = np.rot90(data[i],1)
  plt.imshow(data[i], cmap=plt.cm.coolwarm)
  plt.colorbar()
  plt.show()